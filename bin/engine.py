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
    dispatcher(req,res)
    res.content_type = req.accept[0]
    resp = res.packageresponse()
    logger.info('返回的请求：{}'.format(resp))
    return bytes(resp,'utf-8')

import os,sys
from tools import viewutils as controlutils
from bin.applicationContext import Application

def dispatcher(request,response):
    homepath = Application.serverConfig['homePath']
    url = request.url
    print('\r\n当前url请求为： ' + url + '\r\n')
    if url == '/':
        print('\r\n访问主页面： index.html  \r\n')
        response.content = controlutils.readhtml(homepath+'\\bin\\index.html')
        return
    urlinfolist = url.split('/')
    if len(urlinfolist) > 1:
        response.server = urlinfolist[1]
        serverpath = homepath +'\\webapp\\'+response.server
        if url.endswith('css') | url.endswith('js') | url.endswith('jpg') | url.endswith('png'):
            sourcepath = url[len(response.server)+1:].replace('/','\\')
            print('\r\n下载静态文件路径：' + serverpath+'\\templates'+sourcepath + '\r\n')
            response.content = controlutils.readhtml(serverpath+'\\templates'+sourcepath)
            return
        if os.path.exists(serverpath):
            sys.path.append(serverpath)
            print('\r\n跳转到服务位置： ' + serverpath + '\r\n')
            manage = __import__('manage')
            result = manage.manage(url[url.index(response.server)+len(response.server):],request,response)
            if isinstance(result,str) & result.endswith('.html'):
                response.content = controlutils.readhtml(serverpath+'\\templates\\'+result)
        else:
            response.status = '404'
            response.mark = 'NOTFOUND'