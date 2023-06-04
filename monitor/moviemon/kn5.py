import time
import random
import asyncio

from datetime import datetime

from sql import sql_init
from otg import tg_init, tg_update

from kn.monmov.kinozal import KinozalMonitor
from kn.kinozaltv.site import KinozalSite


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

    deep_check = False

    while True:

        hours = 1
        timeout = 3600 * hours + random.randint(500, 1000)

        kn = KinozalMonitor()

        tm = datetime.now()
        cur_year = tm.year
        pre_year = cur_year - 1

        day = tm.day

        if deep_check:

            deep_check = False

            print(f'deep start')
            for year in (
                    pre_year,
                    cur_year,
            ):
                continue
                # await kn.deep_releases(title_year=year)

            print(f'deep end')

        print(f'main start')
        await kn.main_releases(year=cur_year)
        print(f'main end')

        time.sleep(timeout)

        if datetime.now().day != day:
            deep_check = True


asyncio.run(test())
asyncio.run(main())

         