import asyncio
import httpx
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
sem = asyncio.Semaphore(3)

async def check_chapter(client, idx, title, url):
    async with sem:
        try:
            r = await client.get(url, timeout=20)
            soup = BeautifulSoup(r.text, 'html.parser')
            
            content_el = (
                soup.select_one('.chapter__content') or 
                soup.select_one('#chapter-content') or 
                soup.select_one('.fictioneer-chapter-text') or 
                soup.select_one('.chapter-content') or 
                soup.select_one('article')
            )
            p_tags = content_el.find_all('p') if content_el else []
            clean_paras = [p.get_text(strip=True) for p in p_tags if len(p.get_text(strip=True)) > 15]
            
            if len(clean_paras) > 2:
                first_p = clean_paras[0][:60].encode('ascii', 'ignore').decode()
                print(f"[PUBLIC] [{idx+1}] '{title}' -> ({len(clean_paras)} paras) Sample: {first_p}")
                return True, title, url, len(clean_paras)
            else:
                print(f"[LOCKED] [{idx+1}] '{title}' -> ({len(clean_paras)} paras)")
                return False, title, url, 0
        except Exception as e:
            print(f"[ERROR] [{idx+1}] '{title}' -> Error: {e}")
            return False, title, url, 0

async def main():
    async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=25) as client:
        r = await client.get('https://cherrymist.cafe/story/the-unruly-hero-became-younger/')
        soup = BeautifulSoup(r.text, 'html.parser')
        
        all_links = []
        for g in soup.select('.chapter-group'):
            for a in g.find_all('a', href=True):
                all_links.append((a.get_text(strip=True).encode('ascii', 'ignore').decode(), a['href']))
                
        print(f"Total chapter links found: {len(all_links)}")
        
        tasks = [check_chapter(client, i, t, u) for i, (t, u) in enumerate(all_links[:25])]
        results = await asyncio.gather(*tasks)
        
        public_count = sum(1 for r in results if r[0])
        print(f"\nChecked first 25 chapters: {public_count} are PUBLIC/UNLOCKED!")

if __name__ == '__main__':
    asyncio.run(main())
