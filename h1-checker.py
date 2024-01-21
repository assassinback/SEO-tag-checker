import requests
from bs4 import BeautifulSoup
import re
import time
home_link="https://laureltreepropertymanagement.nesthub.com"
source_code = requests.get(home_link)
soup = BeautifulSoup(source_code.content, 'lxml')
data = []
links = []
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
    if(data[x].find(home_link)>0 or data[x].find("portals")>0):
        continue
    else:
        data[x]=home_link+data[x]
x=0
for x in range(len(data)):
    try:
        source_code = requests.get(data[x])
        soup = BeautifulSoup(source_code.content, 'lxml')
        test=soup.find_all('h1')
        if len(test)>0:
            print("There is/are "+str(len(test))+" h1 Tags on link "+data[x]+", which is/are:\n")
            for page in test:
                  print(page.prettify())
                  print("\n")
        else:
            print("There are "+str(len(test))+" h1 Tags on link "+data[x]+"\n")            
    except Exception as e:
        print("invalid link "+data[x]+"\n")