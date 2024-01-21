import requests
from bs4 import BeautifulSoup
import re
import time
home_link="https://laureltreepropertymanagement.nesthub.com"
source_code = requests.get(home_link)
soup = BeautifulSoup(source_code.content, 'lxml')
data = []
links = []
# test=soup.find_all('h1')
# print(len(test))
# for page in test:
#       print(page.prettify())
def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))


for link in soup.find_all('a', href=True):
    data.append(str(link.get('href')))
remove_duplicates(data)
x=0
for x in range(len(data)):
    x=0
    if(data[x].find("/")>0):
        continue;
    else:
        data.remove(data[x])
x=0
for x in range(len(data)):
    data[x]=home_link+data[x]
x=0
for x in range(len(data)):
    try:
        source_code = requests.get(data[x])
        soup = BeautifulSoup(source_code.content, 'lxml')
        test=soup.find_all('h1')
        print("There are "+str(len(test))+" h1 Tags on this link, which are:\n")
        for page in test:
              print(page.prettify())
              print("\n")
    except Exception as e:
        print("invalid link "+data[x]+"\n")
# flag = True
# remove_duplicates(data)
# while flag:
#     try:
#         for link in links:
#             for j in soup.find_all('a', href=True):
#                 temp = []
#                 source_code = requests.get(link)
#                 soup = BeautifulSoup(source_code.content, 'lxml')
#                 temp.append(str(j.get('href')))
#                 remove_duplicates(temp)

#                 if len(links) > 162: # set limitation to number of URLs
#                     break
#             if len(links) > 162:
#                 break
#         if len(links) > 162:
#             break
#     except Exception as e:
#         print(e)
#         if len(links) > 162:
#             break

# for url in links:
#     print(url)