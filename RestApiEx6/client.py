import requests
import aiohttp
import asyncio
url = "http://www.python.org/dev/peps/pep-8010"

data = requests.get(url)
print(data.content)

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        data = await session.get(url)
        print(await data.text())

asyncio.run(fetch_url(url))