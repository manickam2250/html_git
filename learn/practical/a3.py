
import requests
from bs4 import BeautifulSoup
response=requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup=BeautifulSoup(response.content,"html.parser")
total=soup.find(class_="toc")
url=[]

file=open("/home/manikam/sports1.txt","w")

sports_list=total.find_all("ul")
for i in sports_list:
     
     url.append("https://en.wikipedia.org/wiki/"+i.a["href"].strip("#"))

# print(url)

for j in url:
  file.write(j)
  file.write("\n")


  
        


