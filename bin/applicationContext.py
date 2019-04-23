#encoding=utf-8

import os

class ApplicationContext:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(ApplicationContext,cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self):
        if hasattr(self,'_instance'):return
        self.serverConfig = {}
        self.logConfig = {}
        self.serviceConfig = {}
        self.context = {}

Application = ApplicationContext()