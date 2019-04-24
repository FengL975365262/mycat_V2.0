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

    def startConnector(self):
        while True:
            logger.info('等待连接。。。')
            cli,addr = self.socketServer.accept()
            cli.settimeout(5)
            job = Job(cli,addr)
            logger.info('{}发起请求，正在将任务添加到任务池。。。'.format(addr))
            logger.info('添加成功，当前任务池任务数{}'.format(self.pool.work_queue.count))
            self.pool.execute(job)

class Job:
    def __init__(self ,cli ,addr):
        self.cli = cli
        self.addr = addr

    def run(self):
        logger.info('开始处理任务。。。')
        response = engine.engine(self.cli,self.addr)
        self.cli.send(response)
        logger.info('任务处理成功。。。')
        self.cli.close()