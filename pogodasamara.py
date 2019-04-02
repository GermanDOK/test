import requests 
from bs4 import BeautifulSoup 
from datetime import datetime

def get_html():
    url = "https://yandex.ru/pogoda/samara" 
    responce = requests.get(url)
    return BeautifulSoup(responce.content, "lxml")

def get_temp():
    html = get_html()
    return html.find("span",{"class":"temp__value"}).text  

def get_condition(): 
    html = get_html()
    return html.find("div", {"class":"link__condition"}).text 

def get_wind_speed(): 
    html = get_html()
    return html.find("span", {"class":"wind-speed"}).text 

def get_fact_unit():
    html = get_html()
    return html.find("span", {"class":"fact__unit"}).text 

def get_time():
    html = get_html()
    return html.find("time",  {"class":"fact__time"}).text

def get_term():
    html = get_html()
    return html.find_all("dd", {"class":"term__value"})[4].text

def main(): 
    temp_value = get_temp() 
    condition_value = get_condition() 
    wind_speed_value = get_wind_speed() 
    fact_unit_value = get_fact_unit() 
    time_value = get_time()       
    term_value = get_term()
    
     