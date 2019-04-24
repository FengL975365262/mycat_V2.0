#encoding=utf8

from bin.applicationContext import Application
import os
import threading
from bin.connector import Connector
from tools.logutils import logger

def findWepApps() :
    serviceHomePath = Application.serverConfig.get('workPath', '')
    apps = os.listdir(serviceHomePath)
    Application.serverConfig.update({'apps': apps})
    logger.info('发现服务：{}'.format(apps))

def startConnector():
    serviceConf = Application.serviceConfig[0]
    logger.info('准备在{0}:{1}启动连接器{2}，线程数{3}。。。'.format(serviceConf['host'],serviceConf['port'],Application.serverConfig.get('serverName'),serviceConf['max_thread_num']))
    connector = Connector(Application.serverConfig.get('serverName'),serviceConf['host'],serviceConf['port'],serviceConf['max_thread_num'])
    logger.info('连接器启动成功输入：{0}:{1} 访问主页'.format(serviceConf['host'],serviceConf['port']))
    connector.startConnector()