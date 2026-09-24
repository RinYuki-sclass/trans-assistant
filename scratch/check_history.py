import sqlite3
import os
import shutil

base = r'C:\Users\Innotech\AppData\Local\Google\Chrome\User Data'
os.makedirs('scratch', exist_ok=True)

for prof in ['Default', 'Profile 2', 'Profile 3', 'Profile 4']:
    hist_path = os.path.join(base, prof, 'History')
    if os.path.exists(hist_path):
        try:
            temp_hist = f'scratch/hist_{prof.replace(" ", "_")}.db'
            shutil.copy2(hist_path, temp_hist)
            conn = sqlite3.connect(temp_hist)
            c = conn.cursor()
            c.execute("SELECT url, title FROM urls WHERE url LIKE '%novelupdates%' ORDER BY last_visit_time DESC LIMIT 15")
            rows = c.fetchall()
            if rows:
                print(f"=== {prof} ===")
                for r in rows:
                    print(r[0], "-->", r[1])
            conn.close()
        except Exception as e:
            print(f"Error {prof}: {e}")
