import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
for p in ["9065_2.html", "9065_3.html", "9065_4.html", "9065_306.html"]:
    url = f"https://www.52shuku.net/xiandaidushi/{p}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            p_tags = re.findall(r'<p>(.*?)</p>', html, re.DOTALL)
            clean_p = [re.sub(r'<[^>]+>', '', pt).strip() for pt in p_tags if pt.strip()]
            print(f"=== {p} ({len(clean_p)} p tags) ===")
            for cp in clean_p[:5]:
                print("  ", cp)
            if len(clean_p) > 5:
                print("   ...")
                for cp in clean_p[-2:]:
                    print("  ", cp)
    except Exception as e:
        print(f"=== {p} error: {e} ===")
