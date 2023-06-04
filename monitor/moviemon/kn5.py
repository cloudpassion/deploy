import time
import random
import asyncio

from datetime import datetime

from sql import sql_init
from otg import tg_init, tg_update

from kn.monmov.kinozal import KinozalMonitor
from kn.getmov import GetMovies


sql_init()
tg_init()
# tg_update()


async def test():

    return
    # t = KinozalSite()
    #
    # await t.get_details(1978519)
    # quit()

    kn = KinozalMonitor()

    await kn.main_releases(year=2023)
    # await kn.deep_releases(title_year=2022, start='It Came from Somewhere')
    # await kn.deep_releases(title_year=2023)
    #
    quit()


async def main():

    new_day = False
    new_month = False

    while True:

        hours = 1
        timeout = 3600 * hours + random.randint(500, 1000)

        kn = KinozalMonitor()

        tm = datetime.now()
        cur_year = tm.year
        pre_year = cur_year - 1

        day = tm.day
        month = tm.month

        if new_day:

            print(f'new day start')
            new_day = False

            gm = GetMovies()

            await gm.imdb_upcoming_list()
            await gm.merge_year_files(cur_year)

            print(f'new day end')

        if new_month:

            print(f'new month start')
            for year in (
                    pre_year,
                    cur_year,
            ):
                await kn.deep_releases(title_year=year)
                await kn.main_releases(year=cur_year)

            print(f'new month end')

        print(f'main start')
        await kn.main_releases(year=cur_year)
        print(f'main end')

        time.sleep(timeout)

        if datetime.now().day != day:
            new_day = True

        if datetime.now().month != month:
            new_month = True


asyncio.run(test())
asyncio.run(main())

         