#!/usr/bin/python3

import os
import time

from my.sql import *
from my.tg.tg import *

sql_init()
tg_init()

from my.getfilms import *
from my.kinozal import *

tg_update()

TIMEOUT=3600*1

while True:
    print('tstart')
    main_kinozal_releases()
    print('mex')
    time.sleep(TIMEOUT)

