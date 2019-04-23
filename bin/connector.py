#enconding=utf8

import socket
from tools.logutils import logger
from bin import engine
from tools.threadpool import ThreadPool

class Connector:

    def __init__(self , hostName ,ip ,port,startThreads):
        self.hostName = hostName
        addr = (ip,port)
        self.socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socketServer.bind(addr)
        self.socketServer.listen(startThreads)
        self.pool = ThreadPool()
        logger.info('在{0}:{1}启动连接器{2}，线程数{3}'.format(ip,port,hostName,startThreads))

    def startConnector(self):
        while True:
            cli,addr = self.socketServer.accept()
            job = Job(cli,addr)
            self.pool.execute(job)

class Job:
    def __init__(self ,cli ,addr):
        self.cli = cli
        self.addr = addr

    def run(self):
        response = engine.engine(self.cli,self.addr)
        self.cli.send(response)
        self.cli.close()