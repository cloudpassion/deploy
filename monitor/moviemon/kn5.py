import time
import random
import asyncio

from datetime import datetime

from log import log_stack

from sql import sql_init
from otg import tg_init, tg_update

from kn import KinoMovieMonitor
#.monmov.kinozal import KinozalMonitor
from kn.getmov import GetMovies

from kn.kinozaltv import KinozalSite

sql_init()
tg_init()
# tg_update()


async def test():

    return
    kn = KinozalMonitor()
    await kn.top_releases(
        year='all',
        years=[2020, 2021, 2022, 2023, 2024],
        uploaded_in=['week', 'month', ],
    )
    quit()
    #
    # await kn.top_releases(
    #     year='all',
    #     years=[2020, 2021, 2022, 2023, 2024],
    #     uploaded_in=[
    #         'all', 'week', 'month',
    #     ],
    # )
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

        # kn = KinozalMonitor()
        kn = KinoMovieMonitor()
        gm = GetMovies()

        tm = datetime.now()
        cur_year = tm.year
        pre_year = cur_year - 1
        pp_year = pre_year - 1
        next_year = cur_year + 1

        years = [pp_year, pre_year, cur_year, next_year]
        for year in years:
            gm.merge_year_files(year)

        day = tm.day
        month = tm.month

        if new_day:

            print(f'new day start')
            new_day = False

            await gm.imdb_upcoming_list()
            gm.merge_year_files(cur_year)

            await kn.top_releases(
                year='all',
                years=years,
                uploaded_in=['week', ],
            )

            for lang in ('ru', 'en', ):
                kinorium = GetMovies(
                    kinorium_lang=lang
                )

                await kinorium.kinorium_get_movie_premiers(
                    year=cur_year,
                    tp=['premier', 'online', ]
                )

            print(f'new day end')

        if new_month:

            print(f'new month start')
            for year in (
                    pp_year,
                    pre_year,
                    cur_year,
            ):
                await kn.deep_releases(title_year=year)
                await kn.main_releases(year=year)

            await kn.top_releases(
                year='all',
                years=years,
                uploaded_in=[
                    'all', 'week', 'month',
                ],
            )

            print(f'new month end')

        print(f'main start')
        await kn.main_releases(year=cur_year)
        await kn.hot_picks_releases(year=cur_year)
        print(f'main end')

        time.sleep(timeout)

        if datetime.now().day != day:
            new_day = True

        if datetime.now().month != month:
            new_month = True


try:
    asyncio.run(test())
    asyncio.run(main())
except Exception:
    log_stack.error('init_stack')
    time.sleep(120)

         