#encoding=utf-8

from bin.applicationContext import Application
from bin import service

def initApplication(confdict):
    Application.serverConfig = {'homePath':confdict['homePath'],
                                'serverName':confdict['server']['name'],
                                'serverVersion':confdict['server']['version']
                                }
    Application.serviceConfig = confdict['server']['service']
    Application.logConfig = confdict['log']

def startService():
    service.findWepApps()
    service.startConnector()

