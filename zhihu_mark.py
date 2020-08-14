#!/usr/bin/env python3
import sys
print(sys.version)
#input('ffffff')

import urllib.request as urllib2
from urllib import parse
import re
import json
from bs4 import BeautifulSoup
#import requests

#xxxxxxx
#url='https://www.zhihu.com/question/37787176'
#url2='https://www.zhihu.com/question/51459956'
url = 'https://www.zhihu.com/collection/101668034?page=1'
headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'}
headers['Cookie'] = '___rl__test__cookies=1597412952610; SESSIONID=hHPLaujqHq9rb0nFGDPdDgi58Y2BlXbMepwCTzitCe9; JOID=W1gdB0hpFvxqsvOzS2TVLN96a9tbLyzCHe6MyRYnd7wX-KDpcNqMwTix8rdA8ec7d6LQtiCJIiCrcm_-fPMNoZA=; osd=UV8cCktjEf1nsfm0SmnWJth7ZthRKC3PHuSLyBskfbsW9aPjd9uBwjK287pD--A6eqHasSGEISqsc2L9dvQMrJM=; _zap=34001841-f393-4996-aa83-2da7ce7bdefc; _xsrf=bMLoygxxHRWLghVE7dumXKlTyZnBxa8A; d_c0="AKBs6EDDhA-PTrz7LPbmhIsfWIPtgFiS-ZQ=|1559387592"; __utmv=51854390.100-1|2=registration_date=20160523=1^3=entry_date=20160523=1; _ga=GA1.2.1957404873.1559388790; __utma=51854390.1957404873.1559388790.1581839575.1581842518.22; __utmz=51854390.1581842518.22.18.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/collection/175463711; _gid=GA1.2.1617918194.1597227022; q_c1=11f15a4ab94c4637b19018028d712130|1597371312000|1559388787000; tst=r; OUTFOX_SEARCH_USER_ID_NCOO=1432977460.956664; SESSIONID=O22pVvrQDhHqMYS3ginbAV2jq6hM1hNzNXPyjtKmlyY; JOID=V1EVB0ibXgvvC4s5WpqU31PLH1hO2GU9mFvxQg_ZOkqaQdRmYEQOPrEBjjRZD2V4z2UhKS1-b1FfPxSwcCRjsAw=; osd=VF4cCk-YUQLiDIg2U5eT3FzCEl9N12wwn1j-SwLeOUWTTNNlb00DObIOhzleDGpxwmIiJiRzaFJQNhm3cytqvQs=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1597311312,1597371233,1597393151,1597404642; capsion_ticket="2|1:0|10:1597405409|14:capsion_ticket|44:MjUyYjA4YzA5NDUyNGE4OWJmODYwMTE4ZDllODM1MWI=|954d5a6b990cd713aa1827820ec248ec44e629faece90a24523af017575ee748"; z_c0="2|1:0|10:1597405411|4:z_c0|92:Mi4xSGlZUkF3QUFBQUFBb0d6b1FNT0VEeVlBQUFCZ0FsVk40OFlqWUFDSGRsbGx5OGpwbVRyMDJKWElqbjduSnNwa3JB|53e3e34fa3abc9e89e091c9526c7e87b68b0c7ae5fe8f74c66a00c1107495b8d"; ___rl__test__cookies=1597413023450; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1597415009; _gat_gtag_UA_149949619_1=1; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1597415090|1597410188'
#headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers['Content-Type'] = 'text/html; charset=utf-8'
headers['Host'] = 'www.zhihu.com'
headers['Referer'] = 'https://www.zhihu.com/collection/101668034'
#namedict = {
#        'username': '13520318572',
#        'password': 'a1900876',
#        }
#data = bytes(parse.urlencode(namedict), encoding='utf8')
#xxxxxxx
def request_content(url,contentpattern):
    request=urllib2.Request(url,headers=headers)#, method='post')
    response=urllib2.urlopen(request)
    print(response.getcode())
    content=response.read().decode('utf-8')
    #####################3`
    c1 = BeautifulSoup(content, 'lxml')
#    a1 = c1.find_all('div', class_='zm-item')
#    a1 = c1.find_all('div', class_='CollectionDetailPageHeader-hint')
#    a1 = c1.find_all('h2', class_='ContentItem-title')
    a1 = c1.find_all('div', class_='Card-headerText')
    print('>>>>>1', a1)
    ############
    pattern=re.compile(contentpattern,re.S)
#    items=re.findall(pattern,content)
    items=re.search(pattern,content)
    print('>>>>>2', items)
    input('dddddd')
    return items
#xxxxxxx END

######################################################
######################################################
######################################################
pattern = (
        '<div class="CollectionDetailPageHeader-hint"(.*?)</div>'
        )
#        'Card-headerText">(.*?)</div>'
#        'h2 class=ContentItem-title">(.*?)</a>'
#        '.*?<div class'
#        '<div class="ContentItem AnswerItem.*?title(.*?)"'
#        '<h2 class="ContentItem-tit(.*?)">'
#        '<a(.*?)</a>'
#        noreferrer">(.*?)</a>'
items = request_content(url, pattern)
#print(items)
