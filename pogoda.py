import requests 
from bs4 import BeautifulSoup 

url = "https://yandex.ru/pogoda/moscow" 
responce = requests.get(url) 

html = BeautifulSoup(responce.content, "lxml") 

def get_temp(): 
    return html.find('span class',{"class":temp__value}).value.text


def get_condition(): 
    return html.find("div", {"class":"link__condition"}).text 

def get_wind_speed(): 
    return html.find("span", {"class":"wind-speed"}).text 

def get_fact_unit(): 
    return html.find("span", {"class":"fact__unit"}).text 

def get_time(): 
    return html.find("time", {"class":"fact__time"}).text

def get_term(): 
    return html.find_all("dd", {"class":"term__value"})[4].text

def main(): 
    temp_value = get_temp() 
    condition_value = get_condition() 
    wind_speed_value = get_wind_speed() 
    fact_unit_value = get_fact_unit() 
    time_value = get_time()       
    term_value = get_term()
    
     
     





