
import re
from urllib.parse import urljoin
import aiohttp
import asyncio

def write_todisk():
    with open('urls1000.txt','w') as f:
        for url in master:
            f.write(f'{url}\n')


async def GetBooksUrls(current_page,session):
    async with session.get(current_page) as res:
        html = await res.text()
        pattern = r'<h3><a href="(.*)"\s+.*</h3>'
        urls = re.findall(pattern,str(html))
        for url in urls:
            clean_url = urljoin(current_page,url)
            print(clean_url)
            master.append(clean_url)


async def main():
    curr_page = 'https://books.toscrape.com/catalogue/page-{}.html'
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(GetBooksUrls(curr_page.format(page),session)) for page in range(1,51)]
        results = await asyncio.gather(*tasks)
        return results

master = []
if __name__ == '__main__':
    asyncio.run(main())
    write_todisk()