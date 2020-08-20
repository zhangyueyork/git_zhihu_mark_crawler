#!/usr/bin/env python3
#!coding=utf-8
#
import sys
print(sys.version)
########################
from selenium import webdriver
import time
import random
#from bs4 import BeautifulSoup
import re
print("-"*10,"import end","-"*10)
########
def requestitem(url, pattern):
    driver = webdriver.Chrome(executable_path='/Users/shzy/seleniumwebdriver/chromedriver')
    driver.get(url)
    sleeptime = random.randint(2,10)
    print('time--'+str(sleeptime))
    time.sleep(sleeptime)
    content = driver.page_source
    driver.close()
    ##############
    items = re.findall(pattern, content)
    for i1, item in enumerate(items):
        print(i1, item)
    return items
    ###############


urlx = 'https://www.zhihu.com/collection/101668034?page='
pattern = r'<a target="_blank".*?href="//(.*?)">(.*?)</a>'
for i1 in range(43):
    urli = urlx+str(i1+1)
    print(urli)
    itemi = requestitem(urli, pattern)
    ff = open('alllist.txt', 'a')
    print(urli, file=ff)
    for ii, i11 in enumerate(itemi):
        print(str(i1+1)+'\t'+str(ii)+'\t'+i11[0]+'\t'+i11[1], file=ff)
    ff.close()


#driver = webdriver.PhantomJS()
#soup = BeautifulSoup(content, 'html.parser')
#pattern = '<div class="ContentItem AnswerItem.*?data-zop="{(.*?)}"'
#items = re.search(pattern, soup)
#print(items.group(1))

#driver.find_element_by_id('login_div')
#driver.maximize_window()
#print '111'
#cookie = driver.get_cookies()
#for c in cookie:
#    print c
#print cookie[0]['value']
