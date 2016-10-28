# -*- coding: utf-8 -*-
import sys
import optparse
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

with requests.Session() as c:
    school         = 'YOURSCHOONAMEHERE IE towson'
    url            = 'https://blackboard.'+str(school)+'.edu/webapps/login/'
    USER_ID        = 'YOURUSERNAMEHERE'
    PASSWORD       = 'YOURPASSWORDHERE'
    LOGIN          = 'Login'
    ACTION         = 'login'
    NEW_LOC        = ''
    
    print '[+]Trying to login to ' +str(url) 
    
    #c.get(url)
    #token = c.cookies['authenticity_token']
    login_data = dict(user_id=USER_ID, password=PASSWORD,login=LOGIN,action=ACTION,new_loc=NEW_LOC)
    c.post(url, data=login_data, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","X-Requested-With":'XMLHttpRequest' })

    checkurl = 'https://blackboard.'+str(school)+'.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'
    checklogin = c.get(checkurl)

    print checklogin.content

    if 'Welcome, ' in checklogin.content:
        print "[+]Login Successful"
    else:
        print "[-]Login Unsuccessful"
  