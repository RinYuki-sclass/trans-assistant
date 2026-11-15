import urllib.request
import re

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6xO06IR0G4I2cpl238nSiFJRHODpzSZat7uBL7yDUIz4SLJXSAcsUjnsTumObJgxfrim32hw77a500VKCC6WLSX4kWjdjXNzLWBF5mj9CVN9Vf7Jwi4OWL9CGhV0wAvMNS4AKSg=="
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Final URL:", resp.geturl())
        content = resp.read().decode('utf-8', errors='ignore')
        print("Title:", re.findall(r'<title>(.*?)</title>', content))
except Exception as e:
    print("Error:", e)
