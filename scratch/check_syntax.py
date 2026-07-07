import re

path = r'd:\Nhung\RIDI\trans-assistant\scripts\app.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# First check syntax
try:
    compile(content, path, 'exec')
    print('Syntax OK - no issues found')
except SyntaxError as e:
    print(f'SyntaxError at line {e.lineno}: {e.msg}')
    print(f'Text: {e.text}')
