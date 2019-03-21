import requests 
from bs4 import BeautifulSoup 

url = "https://realtimeyoutube.com" 
responce = requests.get(url) 

html = BeautifulSoup(responce.content, "lxml")

def get_subs_pewdiepie():
    return html.find_all('h2',{"class":"MuiTypography-root-252 MuiTypography-display4-253 t-heading-249"})[0].text
def get_subs_ts():
    return html.find('h2',{"class":"MuiTypography-root-252 MuiTypography-display4-253 t-heading-249"})[1].text


