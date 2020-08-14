#!/usr/bin/python
#!coding=utf-8
#
from __future__ import division
from selenium import webdriver
print "-"*10,"import end","-"*10
########
driver = webdriver.PhantomJS()
#driver.maximize_window()
driver.get('https://mysupervisor.org/viewforum.php?f=4437&sid=c28e9bc02f3ed14b55e50de6e3c11f35')
#driver.find_element_by_id('login_div')
print '111'
cookie = driver.get_cookies()
#for c in cookie:
#    print c
print cookie[0]['value']
