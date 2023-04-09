from .check import CheckUpdate


class TruckersMPUpdater(
    CheckUpdate,
):
    async def update(self):

        await self.get_local_cache()
        await self.check_launcher()
        await self.check_core()
