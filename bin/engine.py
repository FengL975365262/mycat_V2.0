#encoding=utf8

from tools.logutils import logger
from bin import request,response

def engine(cli,addr):
    req = getRequestObj(cli,addr)
    resp = createResponse(req)
    return resp

def getRequestObj(cli,addr):
    try:
        data = cli.recv(1024)
        reqmsg = data.decode('utf-8')
        logger.info('开始解析请求。。。')
        req = request.analysisHTTP(reqmsg)
        logger.info('请求解析成功。。。')
        return req
    except Exception as exp:
        logger.error(str(exp))
        return request.GETRequest()

def createResponse(req):
    res = response.HTTPResponse()
    res.setCookie(req)
    res.content_type = 'text/html'
    res.content = '<h1>hello world</h1>'
    resp = res.packageresponse()
    return bytes(resp,'utf-8')