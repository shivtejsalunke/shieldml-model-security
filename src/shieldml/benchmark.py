import statistics,time
from pathlib import Path
from .crypto import encrypt_file,decrypt_file,verify_file

def benchmark(path,key,iterations=5):
    if iterations<1: raise ValueError('iterations must be positive')
    src=Path(path); samples={'encrypt_ms':[],'verify_ms':[],'decrypt_ms':[]}
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        enc=Path(d)/'artifact.enc'; out=Path(d)/'out.bin'
        for _ in range(iterations):
            t=time.perf_counter(); encrypt_file(src,key,enc); samples['encrypt_ms'].append((time.perf_counter()-t)*1000)
            t=time.perf_counter(); verify_file(enc); samples['verify_ms'].append((time.perf_counter()-t)*1000)
            t=time.perf_counter(); decrypt_file(enc,key,out); samples['decrypt_ms'].append((time.perf_counter()-t)*1000)
    return {k:{'mean':statistics.mean(v),'samples':v} for k,v in samples.items()}
