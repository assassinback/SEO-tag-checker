# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:00:53 2024

@author: Zia-ur-Rehman Khan
"""

import requests
from bs4 import BeautifulSoup
import re
import time
# Home Page link
home_link="https://candlewoodpropertymanagement.nesthub.com"
source_code = requests.get(home_link)
soup = BeautifulSoup(source_code.content, 'lxml')
data = []
links = []
#remove duplicates
def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))
#Find all Links
for link in soup.find_all('a', href=True):
    data.append(str(link.get('href')))
remove_duplicates(data)
#remove useless links
x=0
for x in range(len(data)):
    x=0
    if(data[x].find("/")>0):
        continue;
    else:
        data.remove(data[x])
#fix links that are '/' links
x=0
for x in range(len(data)):
    if(data[x].find(home_link)>0 or data[x].find("portals")>0):
        continue
    else:
        data[x]=home_link+data[x]
#remove duplicates
data = list(dict.fromkeys(data))
#remove useless links
for x in data:
    # try:
    if x.find("javascript:void(0)")>=0 or x.find(".png")>=0 or x.find(".jpg")>=0 or x.find("mailto:")>=0 or x.find("tel:")>=0 or x.find("propertymanagerwebsites")>=0 or x.find("portals")>=0 or x.find("rentvine")>=0 or x.find("zillow")>=0: 
        # print(x)
        data.remove(x)
    # except Exception as e:
    #     print("here")
    #     continue;
#perform checking
x=0

for x in range(len(data)):
    try:
        #get data from links we found on line 17
        source_code = requests.get(data[x])
        soup = BeautifulSoup(source_code.content, 'lxml')
        images=soup.find_all('a')
        # print("here")
        #print missing alt and src attributes
        for script in images:
            if script.has_attr('href') and script.get('href')!="" and script.get('href')!="#":
                # print(script.get('href'))
                try:
                    if script.get('href') in data:
                        continue;
                    request1 = requests.get(script.get('href'))
                    if request1.status_code == 200:    
                        data.append(script.get('href'))
                        continue;
                    else:
                        print("Link with following code on page "+data[x]+" have broken link")
                        print(script)
                except requests.exceptions.ConnectionError as e1:
                    print("Link with following code on page "+data[x]+" have broken link")
                    print(script)
                except Exception as e:
                    # print(e)
                    continue;
            else:
                print("Link with following code on page "+data[x]+" does not have link or href attribute")
                print(script)
            
        print("Link Tested: "+data[x])
    except Exception as e:
        # print(e)
        continue;
        # print("invalid link "+data[x]+"\n")