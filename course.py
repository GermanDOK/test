import requests
import bs4
 
 
url = "http://www.cbr.ru/scripts/XML_daily.asp"
 
res = requests.get(url)
 
html = bs4.BeautifulSoup(res.content, "lxml")
 
 
 
def get_course(id):
    return html.find('valute',{"id":id}).value.text
