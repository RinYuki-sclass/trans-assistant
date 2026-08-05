"""
Scratch test for audio crawler and db modules.
"""
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from audio.crawler import crawl_chapter
from audio.db import init_db, list_projects, upsert_project, list_chapters, delete_project

print("1. Testing DB Initialization...")
init_db()
print("   DB initialized successfully!")

print("\n2. Testing Web Crawler on Hyacinth Bloom...")
url = "https://hyacinthbloom.com/earth-heros-retirement-project/earth-heros-retirement-project-122/"
try:
    res = crawl_chapter(url)
    print(f"   Title: {res['title']}")
    print(f"   Word count: {res['word_count']}")
    print(f"   Paragraphs count: {len(res['paragraphs'])}")
    print(f"   Sample paragraph: {res['paragraphs'][0][:100]}...")
except Exception as e:
    print(f"   Crawler error: {e}")

print("\n3. Testing DB CRUD...")
proj = upsert_project("Test Project", "web_crawler", url, "test-project")
print(f"   Created Project ID: {proj.id}")
delete_project(proj.id)
print("   Deleted Test Project!")
print("\nAll tests completed!")
