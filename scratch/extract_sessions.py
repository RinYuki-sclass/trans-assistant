import os
import re

p = r'C:\Users\Innotech\AppData\Local\Google\Chrome\User Data\Default\Sessions'
for fname in os.listdir(p):
    fpath = os.path.join(p, fname)
    try:
        with open(fpath, 'rb') as f:
            content = f.read()
            # search for novelupdates urls
            matches = re.findall(rb'https?://[^\x00-\x1f\x7f-\xff]*novelupdates[^\x00-\x1f\x7f-\xff]*', content)
            if matches:
                print(f"=== {fname} ({len(matches)} matches) ===")
                seen = set()
                for m in matches:
                    s = m.decode('utf-8', errors='ignore')
                    if s not in seen:
                        seen.add(s)
                        print("  ", s)
    except Exception as e:
        print(f"Error {fname}: {e}")
