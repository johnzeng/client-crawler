# -*- coding:utf-8 -*-

from selenium import webdriver
import sys,traceback
import urllib
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import time
import sys  

reload(sys)
sys.setdefaultencoding('utf-8')

#only one user so far,we can seperate it by ;if we wanna use multiple users
username = os.environ['SINA_USER']
password = os.environ['SINA_PWD']
cookieStr = os.environ['SINA_COOKIE']
cookies = cookieStr.split(';')

driver = webdriver.PhantomJS()

def Check():
  opts = driver.find_elements_by_xpath('//a[@action-type="fl_unfold"]')
  for opt in opts:
    print "find a unfold"
    opt.text
    opt.click()
  data = driver.find_elements_by_xpath('//div[@class="WB_feed_detail clearfix"]')
  for weibo in data:
    #get text
    comments = weibo.find_elements_by_xpath('.//p[@class="comment_txt"]')
    for comment in comments:
      print comment.text

    #get name
    nicknames = weibo.find_elements_by_xpath('.//a[@class="W_texta W_fb"]')
    for nickname in nicknames:
      print nickname.text
      print nickname.get_attribute('href')

    #get time and direct link to weibo
    linkages = weibo.find_elements_by_xpath('.//div[@class="feed_from W_textb"]/a')
    for linkage in linkages:
      print linkage.get_attribute('href')
      dateStr = linkage.get_attribute('date')
      dateLong = float(str(dateStr))
      delta = time.time() - dateLong / 1000
      if delta / 24 / 60 / 60 > 1:
        return
      print linkage.text
      break


  for elem in driver.find_elements_by_xpath('//*[@id="pl_weibo_direct"]/div/div[2]/div/a[@class="page next S_txt1 S_line1"]'):
    print "get next page"
    href = elem.get_attribute('href')
    driver.get(href)
    time.sleep(3)
    Check()

try:
  driver.set_window_size(1124, 850)
  driver.get("http://weibo.com/login.php")
  for cookie in cookies:
    kv = cookie.split('=')
    cookieDict = {
        'name' : kv[0],
        'value' : kv[1],
        'domain' : '.weibo.com',
        'path' : '/'
        }
    driver.add_cookie(cookieDict)

#  driver.get("http://s.weibo.com/weibo/%25E5%2593%25AA%25E9%2587%258C%25E4%25B9%25B0%25E7%258C%25AB&b=1&nodup=1")
  query = urllib.quote("买猫")
  driver.get("http://s.weibo.com/weibo/%s&b=1&nodup=1" % query)
  
  Check()
  
except:
  print "get except"
  tb = traceback.format_exc()
  print tb

driver.quit()
