import asyncio

from log import logger

from app import TruckersMPUpdater

TIMEOUT = 60*10


async def main():

    while True:
        logger.info(f'tr_start')
        updater = TruckersMPUpdater()

        await updater.update()
        await asyncio.sleep(TIMEOUT)


asyncio.run(main())
