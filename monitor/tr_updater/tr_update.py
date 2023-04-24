import asyncio

from log import logger

from app import TruckersMPUpdater

# TIMEOUT = 60*10
# TIMEOUT = 0


async def main():

    # while TIMEOUT:
    logger.info(f'tr_start')
    updater = TruckersMPUpdater()

    await updater.update()
    # await asyncio.sleep(TIMEOUT)


asyncio.run(main())
