import time
from nonebot.default_config import *

# 配置bot唤醒词
NICKNAME = {'X'}
SUPERUSERS = {}
COMMAND_START = {'', '/', '!', '／', '！'}
# COMMAND_START 的值和 SUPERUSERS 一样，可以是 list、tuple、set等任意容器类型，元素类型可以是 str 或正则表达式
HOST = '127.0.0.1'
PORT = 8080
# 用于weather.py中城市adcode及天气api的配置
AMAPAPIKEY = 'X'
ADCODEAPI = 'X'
WEATHERAPI = 'X'
# 配置监听的群组及群员号码
GROUPLIST = []
USERLIST = []
# AUTOREPLY = ''
AUTOREPLY = ['']
# 配置自动回复间隔时间
TIMELASPE = 180  # unit in seconds

CONTENT = ''