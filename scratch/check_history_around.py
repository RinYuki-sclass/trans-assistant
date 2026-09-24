import sqlite3

conn = sqlite3.connect('scratch/hist_Default.db')
c = conn.cursor()
c.execute("SELECT id, url, title, datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime') as visit_time FROM urls WHERE url LIKE '%viewlist/149939%'")
list_visit = c.fetchall()
print("List visit:", list_visit)

if list_visit:
    c.execute("""
        SELECT url, title, datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime') as visit_time 
        FROM urls 
        WHERE url LIKE '%novelupdates%'
        ORDER BY last_visit_time DESC
        LIMIT 50
    """)
    rows = c.fetchall()
    print("\nRecent 50 NovelUpdates URLs:")
    for r in rows:
        print(f"[{r[2]}] {r[1]} -> {r[0]}")
conn.close()
