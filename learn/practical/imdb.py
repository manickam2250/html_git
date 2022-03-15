import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.imdb.com/chart/top/")
soup=BeautifulSoup(response.content,"html.parser")
total=soup.find("tbody",class_="lister-list")
tr=total.find_all("tr")
list=[]
filess=open("/home/manikam/movies.txt","w")
for i in tr:
    list.append(i(class_="titleColumn")[0].a.text)

for j in list:
    filess.write(j)
    filess.write("\n")
filess.close()
    



