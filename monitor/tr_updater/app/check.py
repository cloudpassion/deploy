import os

import ujson as json

from atiny.http import MyHttp
from log import logger


from .const import UPDATE_URL, DAT
from .download import DownloadUpdate


class CheckUpdate(DownloadUpdate):

    async def get_local_cache(self):

        if not os.path.isfile(DAT):
            return

        with open(DAT, 'r') as fr:
            js = json.loads(fr.read())

        for line in js.get('Files'):
            file_path = line.get('FilePath')
            tp = line.get('Type')
            md5 = line.get('Md5')

            self.cache[tp][file_path] = md5

    async def check_launcher(self):
        pass

    async def check_core(self):

        files_url = f'{UPDATE_URL}/files.json'

        http = MyHttp(
            save_cache=True,
            load_cache=False
        )

        resp = await http.get(files_url)

        if resp.error or resp.status != 200:
            return

        with open('files.json', 'wb') as fw:
            fw.write(resp.content)

        js = json.loads(resp.content.decode('utf8'))

        for _file in js.get('Files'):
            file_path = _file.get('FilePath')
            tp = _file.get('Type')
            md5 = _file.get('Md5')

            local_md5 = self.cache[tp].get(file_path)
            if local_md5 and local_md5 == md5:
                continue

            self.to_update[md5] = {
                'path': file_path,
                'type': tp,
            }

        if self.to_update:
            await self.download_core()






        







