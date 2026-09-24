import os
import zlib
import gzip

cache_dir = r'C:\Users\Innotech\AppData\Local\Google\Chrome\User Data\Default\Cache\Cache_Data'

matches = []
for fname in os.listdir(cache_dir):
    fpath = os.path.join(cache_dir, fname)
    if not os.path.isfile(fpath):
        continue
    try:
        with open(fpath, 'rb') as f:
            raw = f.read()
            # check raw
            if b'ALPHA BOTTOM' in raw or b'149939' in raw:
                matches.append((fpath, 'raw', raw))
                continue
            
            # try gzip / deflate
            for offset in [0, 4, 8, 12, 16, 20, 24, 28, 32, 64, 128]:
                try:
                    decomp = zlib.decompress(raw[offset:], -zlib.MAX_WBITS)
                    if b'ALPHA BOTTOM' in decomp or b'149939' in decomp:
                        matches.append((fpath, 'deflate', decomp))
                        break
                except Exception:
                    pass
                try:
                    decomp = gzip.decompress(raw[offset:])
                    if b'ALPHA BOTTOM' in decomp or b'149939' in decomp:
                        matches.append((fpath, 'gzip', decomp))
                        break
                except Exception:
                    pass
    except Exception:
        pass

print(f"Found {len(matches)} matches in cache!")
for fpath, mtype, content in matches:
    print(f"Match in {fpath} ({mtype}), size {len(content)}")
    with open('scratch/found_list_cache.html', 'wb') as out_f:
        out_f.write(content)
