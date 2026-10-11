from pathlib import Path
import hashlib, json, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MAGIC=b'SML1'
def generate_key() -> bytes: return AESGCM.generate_key(bit_length=256)
def _manifest(path: Path) -> Path: return Path(str(path)+'.json')
def encrypt_file(source, key: bytes, output):
    if len(key)!=32: raise ValueError('AES-256 key must be 32 bytes')
    data=Path(source).read_bytes(); nonce=os.urandom(12); ciphertext=AESGCM(key).encrypt(nonce,data,None)
    out=Path(output); out.write_bytes(MAGIC+nonce+ciphertext)
    _manifest(out).write_text(json.dumps({'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'size':out.stat().st_size},indent=2))
    return out
def verify_file(path):
    p=Path(path); m=json.loads(_manifest(p).read_text())
    if p.stat().st_size!=m['size'] or hashlib.sha256(p.read_bytes()).hexdigest()!=m['sha256']: raise ValueError('integrity verification failed')
    raw=p.read_bytes()
    if not raw.startswith(MAGIC) or len(raw)<16: raise ValueError('invalid encrypted envelope')
    return True
def decrypt_file(source,key: bytes,output):
    p=Path(source); verify_file(p); raw=p.read_bytes()
    data=AESGCM(key).decrypt(raw[4:16],raw[16:],None); Path(output).write_bytes(data)
    return Path(output)
