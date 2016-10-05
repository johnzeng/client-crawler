from selenium import webdriver
import sys,traceback
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import time
import sys  

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS()
#only one user so far,we can seperate it by ;if we wanna use multiple users
username = os.environ['SINA_USER']
password = os.environ['SINA_PWD']

try:
  driver.set_window_size(1124, 850)
  driver.get("http://weibo.com/login.php")
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(username)
  driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
  driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

  driver.get("http://s.weibo.com/weibo/%25E5%2593%25AA%25E9%2587%258C%2520%25E4%25B9%25B0%25E7%258C%25AB?topnav=1&wvr=6&b=1")
  data = driver.find_elements_by_xpath('//p[@class="comment_txt"]')
  for i in data:
    print i.text
except:
  print "get excet"
  tb = traceback.format_exc()
  print tb

driver.quit()
