import os
import time
import shutil

from log import logger
from atiny.http.aio import MyHttp

from .const import DOWNLOAD_URL, DAT
from .default import AbstractUpdater


class DownloadUpdate(AbstractUpdater):

    async def download_core(self):

        data_dir = time.strftime('%Y/%m.%d/%Y.%m.%d_%H.%M.%S')
        os.makedirs(data_dir)
        logger.info(f'{self.to_update}')

        info = {}
        links = []

        for md5, data in self.to_update.items():

            link = f'{DOWNLOAD_URL}/files{data.get("path")}'
            tp = data.get('type')

            if info.get(tp):
                info[tp] += f'{md5} {link}\n'
            else:
                info[tp] = f'{md5} {link}\n'

            links.append(
                (link, f'{data_dir}{data.get("path")}')
            )

        for tp in info:
            with open(f'{tp}.txt', 'w') as iw:
                iw.write(info.get(tp))

            shutil.copyfile(f'{tp}.txt', f'{data_dir}/{tp}.txt')

        shutil.copyfile('files.json', f'{data_dir}/files.json')
        shutil.copyfile('files.json', DAT)

        http = MyHttp(save_cache=True, save_headers=False)
        await http.get_urls(
            links, headers=self.headers,
            max_tasks=1,
            tmp_dir='./',
        )

    async def download_launcher(self):
        pass
