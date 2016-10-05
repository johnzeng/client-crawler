from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys

import sys  
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS()
driver.get("http://s.weibo.com/weibo/%25E5%2593%25AA%25E9%2587%258C%2520%25E4%25B9%25B0%25E7%258C%25AB?topnav=1&wvr=6&b=1")
print "now get data"
data = driver.find_elements_by_xpath('//p[@class="comment_txt"]')
for i in data:
  print i.text
driver.quit()
