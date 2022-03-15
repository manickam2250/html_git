import requests
from bs4 import BeautifulSoup

response=requests.get(url="https://www.imdb.com/chart/top/")
soup=BeautifulSoup(response.text,"html.parser")
