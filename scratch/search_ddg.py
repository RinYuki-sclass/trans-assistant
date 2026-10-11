import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'<a class="result__url"[^>]*href="([^"]+)"', html)
            snippets = re.findall(r'<a class="result__snippet"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
            print(f"Results for '{query}':")
            for u in urls[:5]:
                print("  URL:", u)
            for u, s in snippets[:5]:
                print("  Snippet:", u, re.sub(r'<[^>]+>', '', s).strip()[:100])
    except Exception as e:
        print(f"Error {query}: {e}")

search_ddg('site:52shuku.net "在霸总文学里装弯"')
search_ddg('site:dmxs.org "在霸总文学里装弯"')
search_ddg('site:czbooks.net "在霸总文学裡裝彎"')
