import requests 
from bs4 import BeautifulSoup 

url = "https://store.steampowered.com/stats/?l=russian" 
responce = requests.get(url) 

html = BeautifulSoup(responce.content, "lxml")

def get_dota():
    return html.find_all('span',{"class":"currentServers"})[0].text
def get_pubg():
    return html.find_all('span',{"class":"currentServers"})[3].text
