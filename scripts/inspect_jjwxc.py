with open('jjwxc_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))
import re
print("Has tr:", len(re.findall(r'<tr', text)))
print("First 500 chars:", text[:500])
matches = re.findall(r'href=[\'"][^\'"]*chapterid=\d+[\'"]', text)
print("Chapter links:", len(matches))
if matches:
    print("Sample links:", matches[:5])
