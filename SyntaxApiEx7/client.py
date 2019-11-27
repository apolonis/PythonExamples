import aiohttp
import asyncio
url = "http://0.0.0.0:8080/add_user"

# data = requests.get(url)
# print(data.content)

async def post_user(url):
    async with aiohttp.ClientSession() as session:
        my_data = {"name":"Beckham"}
        data = await session.post(url, data=my_data)
        print(await data.text())

asyncio.run(post_user(url))