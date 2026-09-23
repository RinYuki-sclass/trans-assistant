import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/novels_with_synopsis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Targets for both the recent 6 novels and the 9 novels
urls_map = {
    '#4': 'The Demon King Has Face Blindness',
    '#6': 'After Breaking Up with the Alpha Villain, I was Forcibly Marked',
    '#7': 'I Woke Up in the Body of a Newly Appointed Marshal',
    '#8': 'After Transmigrating as the Villain’s Arch-nemesis',
    '#11': 'Possessing the Villain, I Do Good Deeds Daily',
    '#20': 'Stubborn Host, Victim of a Madman’s Forced Love!',
    '#22': 'After I Transmigrated Into a Book, I Was Targeted by the Protagonist Shou',
    '#61': 'Beautiful Mermaid is an Alpha',
    '#68': 'The Villainous Alpha Was Picked up by the Doomsday Boss'
}

for d in data:
    if d['rank'] in urls_map:
        print(f"{d['rank']}. {d['title']}")
        print(f"   NovelUpdates: {d['url']}")
        print(f"   Tên gốc: {d.get('associated', '').replace(chr(10), ' ')}")
        print()
