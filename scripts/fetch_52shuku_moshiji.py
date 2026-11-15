import urllib.request
import re

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeHNxh5Ucv-yCQ1Y6_bTxSlnqQymvdA9fAE6Ewkf3mGrSRH1XlY40n3PJBrzACJS4PNLDpY53TrWLKU6VSErWzK26JvmHEsiat086ssu65zce8-NnYPiMssljpiP6FUgo1ck5rCb4="
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Final URL:", resp.geturl())
        content = resp.read().decode('utf-8', errors='ignore')
        print("Title:", re.findall(r'<title>(.*?)</title>', content))
        print("Snippet:", content[:800])
except Exception as e:
    print("Error:", e)
