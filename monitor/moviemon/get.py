import asyncio
from datetime import datetime

from my.sql import sql_init
from tg.tg import tg_init

sql_init()
tg_init()

from kn.getmov import GetMovies


async def main():

    kn = GetMovies()

    tm = datetime.now()
    cur_year = tm.year
    pre_year = cur_year - 1
    pp_year = pre_year - 1
    next_year = cur_year + 1

    years = [pp_year, pre_year, cur_year, next_year]
    for year in years:
        await kn.kinorium_filmlist(year=year)
        await kn.imdb_year_list(year=year)


asyncio.run(main())
