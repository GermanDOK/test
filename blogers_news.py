import requests
import bs4 

def get_news():
    url = "https://www.rbc.ru/tags/?tag=блогеры"
    content = requests.get(url).content
    soup = bs4.BeautifulSoup(content, "lxml")
    return soup('div', {"class": "search-item js-search-item"})[0:6]

def format_news():
    news_tags = get_news()

    result = ""

    for news in news_tags:
        result += news.text + "\n"

    return result




