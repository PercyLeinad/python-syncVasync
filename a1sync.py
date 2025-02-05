import aiohttp
import time
import asyncio

with open('urls1000.txt','r') as f:
    urls = f.read().split()
    
async def get_response(curr_url,session):
    try:
        async with session.get(curr_url) as res:
            return {'status': res.status, 'url':curr_url}
    except aiohttp.ClientConnectorError as e:
          print('Connection Error', str(e))

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_response(url,session)) for url in urls]
        for task in asyncio.as_completed(tasks):
            result = await task
            print(result)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    stop = time.perf_counter()
    print('Elapsed {:.2f} Secs'.format(stop-start))
