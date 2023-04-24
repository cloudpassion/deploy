from log import logger

from .check import CheckUpdate


class TruckersMPUpdater(
    CheckUpdate,
):
    async def update(self):

        await self.get_local_cache()
        await self.check_launcher()
        await self.check_core()
        await self.clear_update_cache()
        logger.info(f'end update')
