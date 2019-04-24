# coding:utf8

import time


class Logger(object):

    # 单列模式写法
    def __new__(self, *args, **kwargs):
        if not hasattr(self, '_instance'):
            orig = super(Logger, self)
            self._instance = orig.__new__(self, *args, **kwargs)
        return self._instance

    def __init__(self):
        self.logType = "console"
        self.logFilePath = "D:\\workSpace\\python36_workSpace\\mycat_V2.0\\logs"
        self.logLevel = "debug"
        self.logFormat = "[ {0} ][{1}][ {2} ]"
        self.logIO = None
        self.writeLog = self.writeConsole

    def setWriteLog(self):
        if self.logType == 'file':
            fileName = time.strftime('%Y%m%d', time.localtime()) + '.log'
            self.logIO = open(self.logFilePath + '\\' + fileName, 'w')
            self.writeLog = self.writeFile
        else:
            self.writeLog = self.writeConsole

    def __del__(self):
        if self.logIO:
            self.logIO.flush()
            self.logIO.close()

    def debug(self, msg):
        self.log('debug', msg)

    def info(self, msg):
        self.log('info', msg)

    def error(self, msg):
        self.log('error', msg)

    def log(self, level, msg):
        logTime = time.strftime('%H:%M:%S', time.localtime())
        if level == 'info':
            logTpCd = 'I'
        elif level == 'debug':
            logTpCd = 'D'
        elif level == 'error':
            logTpCd = 'E'
        logMsg = self.logFormat.format(logTime, logTpCd, msg)
        self.writeLog(logMsg)

    def writeFile(self, msg):
        self.logIO.write(msg + '\r')
        self.logIO.flush()

    def writeConsole(self, msg):
        print(msg + '\r')

logger = Logger()