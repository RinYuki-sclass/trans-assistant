import sqlite3

conn = sqlite3.connect('scratch/hist_Default.db')
c = conn.cursor()
c.execute("""
    SELECT DISTINCT title, url 
    FROM urls 
    WHERE url LIKE '%novelupdates.com/series/%'
    ORDER BY last_visit_time DESC
    LIMIT 30
""")
rows = c.fetchall()
for i, (title, url) in enumerate(rows, 1):
    clean_title = title.replace(' - Novel Updates', '').strip()
    print(f"{i}. {clean_title} ({url})")
conn.close()
