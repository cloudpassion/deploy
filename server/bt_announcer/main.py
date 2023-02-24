import asyncio

from config import settings

from web import WEB


async def main():
    # server
    server = WEB()

    await server.initialize()

    server.app.run(
        host='0.0.0.0', port=settings.http.port,
    )

    while True:
        await asyncio.sleep(0)


asyncio.run(main())
