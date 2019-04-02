import requests
import bs4 

def get_news():
    url = "http://gamebomb.ru/NEWS"
    content = requests.get(url).content
    soup = bs4.BeautifulSoup(content, "lxml")
    return soup.find_all("div", {"class": "site-news"})

def format_n():
    news_tags = get_news()

    result = ""

    for news in news_tags:
        result += news.text + "\n"

    return result



