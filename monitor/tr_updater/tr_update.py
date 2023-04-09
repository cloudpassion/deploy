import asyncio

from app import TruckersMPUpdater


async def main():

    updater = TruckersMPUpdater()

    await updater.update()

TIMEOUT=60*10

while True:
    print('tr_start')
    asyncio.run(main())
    time.sleep(TIMEOUT)

