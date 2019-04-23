#encoding=utf8

from bin.applicationContext import Application
import os
import threading
from bin.connector import Connector

def findWepApps() :
    serviceHomePath = Application.serverConfig.get('homePath', '')
    apps = os.listdir(serviceHomePath)
    Application.serverConfig.update({'apps': apps})

def startConnector():
    connector = Connector(Application.serverConfig.get('serverName'),'127.0.0.1',8080,5)
    connector.startConnector()