#encoding=utf-8

from bin.applicationContext import Application
from bin import service
from tools.logutils import logger

def initApplication(confdict):
    Application.serverConfig = {'homePath':confdict['homePath'],
                                'workPath':confdict['workPath'],
                                'serverName':confdict['server']['name'],
                                'serverVersion':confdict['server']['version']
                                }
    Application.serviceConfig = confdict['server']['service']
    Application.logConfig = confdict['log']

def initLogger():
    logger.logIO = None
    logger.logType = Application.logConfig['logType']
    logger.logFilePath = Application.logConfig['logFilePath']
    logger.logLevel = Application.logConfig['logLevel']
    logger.logFormat = Application.logConfig['logFormat']
    logger.setWriteLog()

def startService():
    logger.info('开始发现服务。。。')
    service.findWepApps()
    logger.info('服务发现完成，启动连接器。。。')
    service.startConnector()

