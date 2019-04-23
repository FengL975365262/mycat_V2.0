#encoding=utf8

from bin import session

class SessionManage(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(SessionManage,cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self):
        if hasattr(self,'_instance'): return
        self.sessions = {}

    def getSession(self,sessionID):
        return self.sessions.get(sessionID)

    def refreshSessions(self,sessionID):
        if not sessionID :
            sessionObj = session.Session()
            self.sessions.update({sessionObj.SSESSIONID:sessionObj})
        else:
           if sessionID in self.sessions.keys():
                sessionObj = self.sessions.get(sessionID,None)
                if sessionObj.compareSessionTime():
                    sessionObj.changeLastTime()
                else:
                    self.sessions.pop(sessionID)
                    sessionObj = session.Session()
                    self.sessions.update({sessionObj.SSESSIONID: sessionObj})

    def update(self,sessionObj):
        self.sessions.update({sessionObj.SSESSIONID:sessionObj})