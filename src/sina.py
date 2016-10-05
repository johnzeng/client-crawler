from selenium import webdriver
import sys,traceback
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
  data = driver.find_elements_by_xpath('//div[@class="WB_feed_detail clearfix"]')
  for weibo in data:
    comments = weibo.find_elements_by_xpath('//p[@class="comment_txt"]')
    for comment in comments:
      print comment.text
  for elem in driver.find_elements_by_xpath('//*[@id="pl_weibo_direct"]/div/div[2]/div/a[@class="page next S_txt1 S_line1"]'):
    href = elem.get_attribute('href')
    driver.get(href)
    time.sleep(2)
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

  driver.get("http://s.weibo.com/weibo/%25E5%2593%25AA%25E9%2587%258C%25E4%25B9%25B0%25E7%258C%25AB&b=1&nodup=1")
  
  Check()
  
except:
  print "get excet"
  tb = traceback.format_exc()
  print tb

driver.quit()
