#encoding=utf-8

import json
from bin import server

with open('mycat_conf.json') as conf:
    confdict = json.load(conf)
server.initApplication(confdict)
server.startService()