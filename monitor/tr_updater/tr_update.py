import asyncio

from log import logger

from app import TruckersMPUpdater


async def main():

    logger.info(f'tr_start')
    updater = TruckersMPUpdater()

    await updater.update()


asyncio.run(main())
