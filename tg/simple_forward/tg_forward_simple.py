import asyncio

from relethon.client import MyTelegramClient


tg_client = MyTelegramClient()


async def main():

    await tg_client.incoming_forward()
    await tg_client.client_start()


asyncio.run(main())
