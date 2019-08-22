#/usr/bin/env python
'''
@filename wxbot
@by moji
@version 3.0
@py version 3.7.2
@os Linux
'''
import itchat, time
import re
import os
import requests
import urllib
from itchat.content import *
from bs4 import BeautifulSoup
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Inches
import urllib3.contrib.pyopenssl
from JRspider import *

urllib3.contrib.pyopenssl.inject_into_urllib3() #禁用ssl验证
requests.packages.urllib3.disable_warnings()   # 禁用安全请求警告
@itchat.msg_register([SHARING])
def text_reply(msg):
    link=str(msg.url)
    print(link)
    jrobj = JinRi().get(link)
    docName = jrobj.get_docx()
    if docName is not None:
        os.system(r"onedrivecmd put document/%s od:/LXG/" % docName)
        if os.path.exists(r"document/%s" % docName):
            msg.user.send(u"文档已生成\n[%s]" % docName)

#@itchat.msg_register([TEXT, MAP, CARD, NOTE])
#def text_reply(msg):
       # msg.user.send(u'木子机器人值班中：%s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )


#@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])

# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')
# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))
itchat.auto_login(enableCmdQR=2)
itchat.run(True)
