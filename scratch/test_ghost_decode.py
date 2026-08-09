import sys
sys.path.insert(0, 'scripts')
from audio.crawler import crawl_chapter

print("Testing Cherry Mist chapter uh-1 with ghost content decoder...")
try:
    res = crawl_chapter('https://cherrymist.cafe/chapter/uh-1/')
    print(f"Title: {res['title']}")
    print(f"Word count: {res['word_count']}")
    print(f"Paragraphs count: {len(res['paragraphs'])}")
    if res['paragraphs']:
        print(f"First paragraph: {res['paragraphs'][0][:120]}")
        print(f"Last paragraph: {res['paragraphs'][-1][:120]}")
except Exception as e:
    print(f"Error: {e}")
