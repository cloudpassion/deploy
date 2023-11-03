from atiny.reos.cd import cd
cd(__file__)

import asyncio

from log import logger, log_stack

try:
    import uvloop
    uvloop.install()
except ImportError:
    logger.info(f'uvloop not found')


from datetime import datetime, timedelta
from collections import deque

from rerogram.loader import setup_django
from rerogram.client import MyTelegramClient

from log import logger
from config import settings


async def chunked_check_history(
        tg_client, chat_id, limit=98, to_watch=30000,
        sleep=0.0,
):

    while to_watch >= 0:

        await tg_client.on_start(
            None,
            tg_client.db_insert_messages(
                chat_id,
                tg_client.discussion_fwd_data,
                limit=limit,
                sleep=sleep,
                offset=to_watch,
            )
        )

        to_watch -= limit


async def main():

    tg_client = MyTelegramClient()

    # chunked if more than ~500 new message
    for _fwd_data in (
            # (98, 500, settings.discussion.forward.sh1_chat.from_chat_id),
            # (98, 3000, settings.discussion.forward.sh2_chat.from_chat_id),
            # (98, 700, settings.discussion.forward.oss_chat.from_chat_id),
            # (98, 700, settings.discussion.forward.oss_chat.from_chat_id),

            # (98, 10000, settings.discussion.forward.sgus_chat.from_chat_id),
            None,
    ):
        if not _fwd_data:
            logger.info(f'skip.fwd.1')
            continue

        logger.info(f'1.{_fwd_data=}')

        limit = _fwd_data[0]
        to_watch = _fwd_data[1]
        w_chat_id = _fwd_data[2]
        await chunked_check_history(
            tg_client,
            chat_id=w_chat_id,
            limit=limit,
            to_watch=to_watch,
            sleep=0.2,
        )

    # rewatch for get newest before monitor
    # chat_id from settings file settings.discussion.forward
    for _fwd_data in (
        # name, limit, chat_id (*optional*)

        # def
        ('sh2_chat', 128),
        ('sh1_chat', 128),
        ('oss_chat', 128),
        ('sgus_chat', 128),

        ('shduet_channel', 64),
        ('ukprok_channel', 64),

        ('spb_channel', 32, settings.spb.tg.channel_id),
        ('spb_chat', 64),
        None,
    ):
        if not _fwd_data:
            logger.info(f'skip.fwd.2')
            continue

        logger.info(f'2.{_fwd_data=}')

        re_chat_name = _fwd_data[0]
        to_watch = _fwd_data[1]

        try:
            re_chat_id = _fwd_data[2]
        except IndexError:
            re_chat = getattr(settings.discussion.forward, re_chat_name)
            re_chat_id = getattr(re_chat, 'from_chat_id')

        await tg_client.on_start(
            None,
            tg_client.db_insert_messages(
                re_chat_id,
                tg_client.discussion_fwd_data,
                offset_id='last',
                limit=to_watch,
            )
        )

    try:
        lazy = settings.log.lazy
    except Exception as exc:
        logger.info(f'lz: {exc=}')
        lazy = False

    await tg_client.on_start(
        None,
        tg_client.events(
            lazy=lazy
        )
        )
    await tg_client.client_start()


asyncio.run(main())
