import urllib.request
import re

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFj_yHwnGRpv1_8qRArvzZwQ3NRYkVRQhNc23WJnisxTrf9qIoDX_boX5G5OlOlFjNDoGGxDhMJz_sS28YxayN13Bbsa4NWg3StE07Nhu_Fu1OZrgdk29QzLzG7gVAc91iwcY4t"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Final URL:", resp.geturl())
        content = resp.read().decode('utf-8', errors='ignore')
        print("Title:", re.findall(r'<title>(.*?)</title>', content))
except Exception as e:
    print("Error:", e)
