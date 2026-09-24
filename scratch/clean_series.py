import sqlite3

conn = sqlite3.connect('scratch/hist_Default.db')
c = conn.cursor()
c.execute("""
    SELECT url, title, datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime') as visit_time
    FROM urls 
    WHERE url LIKE '%novelupdates.com/series/%'
    ORDER BY last_visit_time DESC
""")
rows = c.fetchall()

seen = set()
unique_series = []
for url, title, visit_time in rows:
    # clean base url
    base_url = url.split('?')[0].rstrip('/') + '/'
    if base_url not in seen:
        seen.add(base_url)
        clean_title = title.replace(' - Novel Updates', '').replace('Just a moment...', '').strip()
        unique_series.append((clean_title, base_url, visit_time))

with open('scratch/unique_series.txt', 'w', encoding='utf-8') as f:
    for i, (t, u, vt) in enumerate(unique_series, 1):
        f.write(f"{i}. {t} | {u} | {vt}\n")

print(f"Total unique series found in history: {len(unique_series)}")
conn.close()
