# -*- coding: utf-8 -*-
import sys
import optparse
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

with requests.Session() as c: #startup requests as c
    school         = 'YOURSCHOONAMEHERE' #school name (IE unomaha,umd,ASU)       #variables to be posted 
    url            = 'https://blackboard.'+str(school)+'.edu/webapps/login/'
    USER_ID        = 'YOURUSERNAMEHERE'
    PASSWORD       = 'YOURPASSWORDHERE'
    LOGIN          = 'Login'
    ACTION         = 'login'
    NEW_LOC        = ''
    
    print '[+]Trying to login to ' +str(url)  #verify that login url is desired one by printing it
    
    #c.get(url)
    #token = c.cookies['authenticity_token']
    login_data = dict(user_id=USER_ID, password=PASSWORD,login=LOGIN,action=ACTION,new_loc=NEW_LOC) #create dict to be posted
    c.post(url, data=login_data, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","X-Requested-With":'XMLHttpRequest' })
    # post login data / headers
    checkurl = 'https://blackboard.'+str(school)+'.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1' #navigate to landing page after loging in to check for Welcome message
    checklogin = c.get(checkurl)

    #print checklogin.content 

    if 'Welcome, ' in checklogin.content: #if welcome message is present, login was successful
        print "[+]Login Successful"
    else:                                  #if not the login went wrong or too many requests were sent which blackboard will block
        print "[-]Login Unsuccessful"
  
