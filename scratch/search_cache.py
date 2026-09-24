import os

cache_dir = r'C:\Users\Innotech\AppData\Local\Google\Chrome\User Data\Default\Cache\Cache_Data'
matches = []

if os.path.exists(cache_dir):
    for fname in os.listdir(cache_dir):
        fpath = os.path.join(cache_dir, fname)
        if os.path.isfile(fpath) and os.path.getsize(fpath) < 10*1024*1024:
            try:
                with open(fpath, 'rb') as f:
                    data = f.read()
                    if b'ALPHA BOTTOM' in data or b'149939' in data:
                        matches.append((fpath, len(data)))
            except Exception:
                pass

print(f"Found {len(matches)} cache files matching!")
for p, s in matches:
    print(p, s)
