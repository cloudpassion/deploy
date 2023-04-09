import asyncio

from app import TruckersMPUpdater


async def main():

    updater = TruckersMPUpdater()

    await updater.update()


asyncio.run(main())
