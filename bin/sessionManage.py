#encoding=utf8

from bin import session
from tools.logutils import logger

class SessionManage(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(SessionManage,cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self):
        self.sessions = {}

    def getSession(self,sessionID):
        logger.info('当前session总量：{}'.format(self.sessions))
        return self.sessions.get(sessionID)

    def refreshSessions(self,sessionID):
        if not sessionID or sessionID not in self.sessions.keys():
            sessionObj = session.Session()
            self.sessions.update({sessionObj.SSESSIONID: sessionObj})
            logger.info('当前session总量：{}'.format(self.sessions))
        else:
           if sessionID in self.sessions.keys():
                sessionObj = self.sessions.get(sessionID,None)
                if sessionObj.compareSessionTime():
                    sessionObj.changeLastTime()
                else:
                    self.sessions.pop(sessionID)
                    sessionObj = session.Session()
                    self.sessions.update({sessionObj.SSESSIONID: sessionObj})
        logger.info('当前session总量：'.format(self.sessions))
        return sessionObj.SSESSIONID

    def update(self,sessionObj):
        self.sessions.update({sessionObj.SSESSIONID:sessionObj})

ssmanage = SessionManage()