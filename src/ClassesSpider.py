# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
import urlparse
import sys,traceback
import sqlite3
import plistlib
import logging  
import logging.handlers  

handler = logging.StreamHandler(sys.stdout)
fmt = '%(asctime)s |%(filename)s:%(lineno)s |%(name)s :%(message)s'  
  
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
  
logger = logging.getLogger('Tester')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG) 

commentRe = re.compile('comment_txt.*?>(.*?)<\\\/p>', re.S)

#This is the base Spider, you should only use this spider
class Spider:
    def __init__(self):
        self.searchedUrl = set([])

    def pullWeb(self, url):
        try:
            if url in self.searchedUrl:
              return ""
            request = urllib2.Request(url,)
            response = urllib2.urlopen(request)
            rspMsg = response.read()
            self.searchedUrl.add(url)
            return rspMsg
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                logger.error(e.code)
            if hasattr(e,"reason"):
                logger.error(e.reason)
            logger.error("request:%s" % url)
            return ""
    def tryOne(self):
        webStr = self.pullWeb("http://s.weibo.com/weibo/猫咪Refer=STopic_box")
        comments = commentRe.findall(webStr)
        print comments
        for i in comments:
            print "------------------------------------"
            print i

if __name__  == '__main__':
    spider = Spider()
    spider.tryOne()

