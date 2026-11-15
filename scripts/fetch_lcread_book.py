import urllib.request
import re

url = "https://lcread.com/bookpage/273136/index.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('gbk', errors='ignore')
        print("Length:", len(content))
        title = re.findall(r'<title>(.*?)</title>', content)
        print("Title:", title)
        # Search for author
        author = re.findall(r'作\s*者[：:]\s*(?:<[^>]+>)?([^<\n\r]+)', content)
        print("Author:", author)
        # Search for chapters
        chapters = re.findall(r'<a[^>]*href=[\'"]([^\'"]*rc\.html)[\'"][^>]*>(.*?)</a>', content)
        print("Total chapters found:", len(chapters))
        for ch in chapters[:10]:
            print("  ", ch)
        if len(chapters) > 10:
            print("   ...")
            for ch in chapters[-5:]:
                print("  ", ch)
        
        # Look for status / word count
        info = re.findall(r'<div[^>]*class=[\'"][^\'"]*info[^\'"]*[\'"][^>]*>(.*?)</div>', content, re.DOTALL)
        if info:
            print("Info:", re.sub(r'<[^>]+>', ' ', info[0])[:300])
except Exception as e:
    print("Error:", e)
