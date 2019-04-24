#encoding=utf-8

import json
from bin import server
from tools.logutils import logger

with open('mycat_conf.json') as conf:
    logger.info('读取配置文件mycat_conf.json')
    confdict = json.load(conf)

logger.info('配置文件读取成功，开始初始化全局上下文ApplicationContext。。。')
server.initApplication(confdict)

logger.info('全局上下文配置成功，开始配置日志组件。。。')
server.initLogger()

logger.info('所有组件配置成功，开始启动服务。。。')
server.startService()