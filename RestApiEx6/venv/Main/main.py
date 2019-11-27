import time
import asyncio
async def longTask(sleepTime):
    print(f'begin {sleepTime}')
    await asyncio.sleep(sleepTime)
    print(f'awake{sleepTime}')

async def runTask():
    await longTask(2)

# asyncio.run(longTask(2))
asyncio.run(runTask())