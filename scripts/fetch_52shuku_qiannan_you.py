import urllib.request
import re

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeXwCCNne-LHbgxUAijjqddckPcqDCemKXLI17Wj-3Jn-ZMXg6VrPzdKrRmlIkk2if_jT6BX0esC2-PoY81_r_PuyqQuybZnlTjZklKb970m7yGipyVLoMv9AnuGhwAQ=="
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Final URL:", resp.geturl())
        content = resp.read().decode('utf-8', errors='ignore')
        print("Title:", re.findall(r'<title>(.*?)</title>', content))
except Exception as e:
    print("Error:", e)
