import pytest
from shieldml.crypto import generate_key,encrypt_file,decrypt_file,verify_file

def test_round_trip(tmp_path):
 src=tmp_path/'model.bin'; src.write_bytes(b'fixture'); key=generate_key(); enc=tmp_path/'model.enc'; out=tmp_path/'out.bin'
 encrypt_file(src,key,enc); assert verify_file(enc); decrypt_file(enc,key,out); assert out.read_bytes()==src.read_bytes()
def test_tampering(tmp_path):
 src=tmp_path/'m'; src.write_bytes(b'model'); enc=tmp_path/'m.enc'; encrypt_file(src,generate_key(),enc); raw=bytearray(enc.read_bytes()); raw[-1]^=1; enc.write_bytes(raw)
 with pytest.raises(ValueError,match='integrity'): verify_file(enc)
def test_bad_key(tmp_path):
 with pytest.raises(ValueError): encrypt_file(tmp_path/'missing',b'bad',tmp_path/'out')
