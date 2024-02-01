# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:44:27 2024

@author: ziakh
"""

# import requests
# from bs4 import BeautifulSoup
# import re
# import time
# # Home Page link
# home_link="https://laureltreepropertymanagement.nesthub.com"
# source_code = requests.get(home_link)
# soup = BeautifulSoup(source_code.content, 'html.parser')
# data = []
# links = []
# patt = re.compile("font-size:(\d+)")
# #remove duplicates
# def remove_duplicates(l): # remove duplicates and unURL string
#     for item in l:
#         match = re.search("(?P<url>https?://[^\s]+)", item)
#         if match is not None:
#             links.append((match.group("url")))
# #Find all Links
# for link in soup.find_all('a', href=True):
#     data.append(str(link.get('href')))
# remove_duplicates(data)
# #remove useless links
# x=0
# for x in range(len(data)):
#     x=0
#     if(data[x].find("/")>0):
#         continue;
#     else:
#         data.remove(data[x])
# #fix links that are '/' links
# x=0
# for x in range(len(data)):
#     if(data[x].find(home_link)>0 or data[x].find("portals")>0):
#         continue
#     else:
#         data[x]=home_link+data[x]
# #remove duplicates
# data = list(dict.fromkeys(data))
# #remove useless links
# for x in data:
#     # try:
#     if x.find("javascript:void(0)")>=0 or x.find(".png")>=0 or x.find(".jpg")>=0 or x.find("mailto:")>=0 or x.find("tel:")>=0 or x.find("propertymanagerwebsites")>=0 or x.find("portals")>=0 or x.find("rentvine")>=0 or x.find("zillow")>=0: 
#         # print(x)
#         data.remove(x)
#     # except Exception as e:
#     #     print("here")
#     #     continue;
# #perform checking
# x=0


from bs4 import BeautifulSoup
import re
import requests
def foo(tag):
    import re
    tag_style = tag.attrs.get('style')
    return bool(re.search(r'font-size.*:[^:]*px', tag_style)) if tag_style else False
home_link="https://laureltreepropertymanagement.nesthub.com"
source_code = requests.get(home_link)
soup = BeautifulSoup(source_code.content,'html.parser')
# tags = soup.find_all()
# for i in tags:
#     if i.string=="None" or i.string is None or i is None:
#         continue;
#     print(i)
    
    
    
# font_spans = [ data for data in soup.select('span') if 'font-size' in str(data) ]
# output = []
# for i in font_spans:
#     tup = ()
#     fonts_size = re.search(r'(?is)(font-size:)(.*?)(px)',str(i.get('style'))).group(2)
#     tup = (str(i.text).strip(), fonts_size.strip())
#     output.append(tup)
# css_link = find_list_resources("link","href",soup)
# print(output)

# def find_list_resources (tag, attribute,soup):
#    list = []
#    for x in soup.findAll(tag):
#        try:
#            list.append(x[attribute])
#        except KeyError:
#            pass
#    return(list)