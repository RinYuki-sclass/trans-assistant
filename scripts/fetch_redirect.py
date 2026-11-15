import urllib.request
import re

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc7irHI-vkO9HzpX-F553bgU4_OfqrEnMHUyg0mjbT-g3PyYjMNIWFjPh0PfqhzqKwuKn1d0dbk7INQHvIQkWTCDZJR3uJmjGZ71Z3cBZRwr6vzEIMCCMrgITeairKUWB-hsEaVyLp"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        final_url = resp.geturl()
        print("Final URL:", final_url)
        content = resp.read().decode('gbk', errors='ignore')
        print("Length:", len(content))
        print("Title:", re.findall(r'<title>(.*?)</title>', content))
        print(content[:1000])
except Exception as e:
    print("Error:", e)
