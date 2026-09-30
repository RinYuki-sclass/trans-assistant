import glob
import json

dir_path = glob.glob('d:/Nhung/RIDI/trans-assistant/novel_projects/*khi*')[0]

# Update config.json style_guide
config_file = f'{dir_path}/config.json'
with open(config_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

rule_str = '- Sở Tư Thừa (楚司承): Luôn dùng đại từ ngôi thứ 3 trong văn trần thuật là "anh".'
if config.get('style_guide'):
    if rule_str not in config['style_guide']:
        config['style_guide'] += f'\n{rule_str}'
else:
    config['style_guide'] = rule_str

with open(config_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

# Update glossary.json with pronoun entry
glossary_file = f'{dir_path}/memory/glossary.json'
with open(glossary_file, 'r', encoding='utf-8') as f:
    glossary = json.load(f)

found = False
for item in glossary:
    if item.get('original') in ['楚司承 (ngôi thứ 3)', '[Ngôi 3] Sở Tư Thừa']:
        item['translation'] = 'anh'
        found = True
        break

if not found:
    glossary.insert(0, {
        'original': '[Ngôi 3] Sở Tư Thừa',
        'translation': 'anh',
        'hanviet': '',
        'category': 'pronoun',
        'confidence': 1.0,
        'approved': True,
        'notes': 'Sở Tư Thừa luôn dùng "anh" ở ngôi thứ 3 trong văn trần thuật'
    })

with open(glossary_file, 'w', encoding='utf-8') as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print('Updated config.json and glossary.json successfully!')
