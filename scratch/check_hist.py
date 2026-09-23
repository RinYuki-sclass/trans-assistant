import os, glob, sqlite3, shutil

user_data = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data')
profiles = glob.glob(os.path.join(user_data, 'Default')) + glob.glob(os.path.join(user_data, 'Profile *'))

for idx, prof in enumerate(profiles):
    hist = os.path.join(prof, 'History')
    if os.path.exists(hist):
        temp_hist = f'scratch/temp_hist_{idx}.db'
        try:
            shutil.copyfile(hist, temp_hist)
            conn = sqlite3.connect(temp_hist)
            cursor = conn.cursor()
            cursor.execute("SELECT url, title, last_visit_time FROM urls WHERE url LIKE '%141600%' ORDER BY last_visit_time DESC")
            rows = cursor.fetchall()
            for r in rows:
                print(f"[{os.path.basename(prof)}]", r[0], "-->", r[1])
            conn.close()
            if os.path.exists(temp_hist):
                os.remove(temp_hist)
        except Exception as e:
            print(f"Error {prof}:", e)
