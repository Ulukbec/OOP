import os

import tcolors
import colorama
from envparse import env

import envparse

env.read_envfile('options.env')
tcolors.cprint(tcolors.Color.BRIGHT_BLUE + colorama.Back.BLACK + os.environ.get('USER_NAME'), os.environ.get('PASSWORD'))
# print(os.environ.get('PASSWORD'))





