import requests 
from bs4 import BeautifulSoup 

url = "https://realtimeyoutube.com" 
responce = requests.get(url) 

html = BeautifulSoup(responce.content, "lxml")

def get_subs():
    return html.find('h2',{"class":"MuiTypography-root-252 MuiTypography-display4-253 t-heading-249"})
