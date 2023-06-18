import asyncio
from datetime import datetime

from my.sql import sql_init
from tg.tg import tg_init

sql_init()
tg_init()

from kn.getmov import GetMovies


async def test():

    for lang in ('ru', 'en', ):
        kn = GetMovies(
            kinorium_lang=lang
        )

        await kn.kinorium_get_movies_upcoming(
            year=2023,
            # max_page=1,
            # skip_write=True
        )

    quit()


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

    for lang in ('ru', 'en', ):
        kn = GetMovies(
            kinorium_lang=lang
        )

        await kn.kinorium_get_movie_premiers(
            year=cur_year,
            # max_page=1,
            # skip_write=True
        )

asyncio.run(test())
asyncio.run(main())
