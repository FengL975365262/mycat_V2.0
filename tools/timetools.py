#encoding=utf8

import time

class TimeTools:

    def __init__(self):
        self.UNIT_SECOND = 0
        self.UNIT_MINUTE = 1
        self.UNIT_HOUR = 2
        self.UNIT_DAY = 3
        self.UNIT_MONTH = 4
        self.UNIT_YEAR = 5

    def getTime(self):
        return time.time()

    def getLocalTime(self,useTime):
        if not useTime : useTime = self.getTime()
        return time.localtime(useTime)

    def getFormatTime(self,useTime,useFormat):
        if not useTime : useTime = self.getLocalTime(useTime)
        if not useFormat : useFormat = '%Y%m%d%H%M%S'
        return time.strftime(useFormat,useTime)

    def getYYYYMMDD(self,useTime):
        return self.getFormatTime(useTime,'%Y%m$d')

    def getHHMMSS(self,useTime):
        return self.getFormatTime(useTime,'%H%M%S')

    def getYYYYmmddHHMMSS(self,useTime):
        return self.getFormatTime(useTime,'%Y%m%d%H%M%S')

    def changeTime(self,useTime,num,TIME_UNIT):
        if not useTime : useTime = self.getTime()
        if num == 0 : return useTime
        if TIME_UNIT == self.UNIT_SECOND : return useTime + num
        if TIME_UNIT == self.UNIT_MINUTE : return useTime + 60 * num
        if TIME_UNIT == self.UNIT_HOUR : return useTime + 60 * 60 * num
        if TIME_UNIT == self.UNIT_DAY : return useTime + 60 * 60 * 24 * num
        if TIME_UNIT == self.UNIT_MONTH : return useTime + 60 * 60 * 24 * 30 * num
        if TIME_UNIT == self.UNIT_MONTH: return useTime + 60 * 60 * 24 * 30 * 12 * num

    def compareTime(self , cpTime , adTime):
        return cpTime < adTime


TimeTool = TimeTools()