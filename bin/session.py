#encoding=utf8

from tools.timetools import TimeTool
import random

class Session(object):

        def __init__(self):
            self.SSESSIONID = self.createSessionID()
            self.LIFETIME = 30
            self._LASTTIME = TimeTool.changeTime(TimeTool.getTime(),self.LIFETIME,TimeTool.UNIT_MINUTE)
            self.CONTEXT = {}

        def createSessionID(self):
            randnum = random.randrange(99999999999999)
            timestr = TimeTool.getHHMMSS(None)
            return str(randnum) + str(timestr)

        def updateSession(self,context):
            self.CONTEXT.update(context)

        def clearSession(self):
            self.CONTEXT = {}

        def compareSessionTime(self):
            return TimeTool.compareTime(TimeTool.getTime(),self._LASTTIME)

        def changeLastTime(self):
            self._LASTTIME = TimeTool.changeTime(TimeTool.getTime(), self.LIFETIME, TimeTool.UNIT_MINUTE)