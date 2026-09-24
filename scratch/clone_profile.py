import os
import shutil

src_root = r'C:\Users\Innotech\AppData\Local\Google\Chrome\User Data'
dst_root = r'd:\Nhung\RIDI\trans-assistant\scratch\chrome_profile'

os.makedirs(dst_root, exist_ok=True)

# Copy Local State
if os.path.exists(os.path.join(src_root, 'Local State')):
    shutil.copy2(os.path.join(src_root, 'Local State'), os.path.join(dst_root, 'Local State'))

# Create Default dir in dst
dst_default = os.path.join(dst_root, 'Default')
os.makedirs(dst_default, exist_ok=True)

# Copy Network folder (Cookies)
src_network = os.path.join(src_root, 'Default', 'Network')
dst_network = os.path.join(dst_default, 'Network')
os.makedirs(dst_network, exist_ok=True)

for fname in ['Cookies', 'Network Persistent State']:
    fsrc = os.path.join(src_network, fname)
    if os.path.exists(fsrc):
        try:
            shutil.copy2(fsrc, os.path.join(dst_network, fname))
            print(f"Copied {fname}")
        except Exception as e:
            print(f"Error copying {fname}: {e}")

# Copy Preferences if exists
pref_src = os.path.join(src_root, 'Default', 'Preferences')
if os.path.exists(pref_src):
    try:
        shutil.copy2(pref_src, os.path.join(dst_default, 'Preferences'))
        print("Copied Preferences")
    except Exception as e:
        print(f"Error copying Preferences: {e}")

print("Done setting up profile clone.")
