#encoding=utf8

from tools.logutils import logger
from bin import request,response

def engine(cli,addr):
    data = cli.recv(1024)
    reqmsg = data.decode('utf-8')
    print('\r\n请求原文为：\r\n' + reqmsg + '\r\n')
    # if not reqmsg: pubInfo(cliSocket)
    res = response.HTTPResponse()
    req = request.analysisHTTP(reqmsg);
    res.content_type = req.accept[0]
    res.content = '<h1>hello world</h1>'
    resp = res.packageresponse()
    return bytes(resp,'utf-8')
