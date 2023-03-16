import asyncio
#import logging

from config import settings

from web import WEB

#logging.getLogger("sanic.access").propagate = False
#logging.getLogger("sanic.root").propagate = False

async def main():
    # server
    server = WEB()

    await server.initialize()
    
    if __name__ == "__main__":
        server.app.run(
            host=settings.http.host, port=settings.http.port,
        )

        while True:
            await asyncio.sleep(0)


asyncio.run(main())

