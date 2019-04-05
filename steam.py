import requests 
from bs4 import BeautifulSoup 

url = "https://steamcharts.com" 
responce = requests.get(url) 

html = BeautifulSoup(responce.content, "lxml")

def get_dota2():
    return html.find_all('td',{"class":"num"})[5].text
def get_pubg():
    return html.find_all('td',{"class":"num"})[8].text
def get_csgo():
    return html.find_all('td',{"class":"num"})[11].text
def get_warframe():
    return html.find_all('td',{"class":"num"})[14].text


