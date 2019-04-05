import requests
import bs4 

def get_news():
    url = "https://kanobu.ru/tech/"
    content = requests.get(url).content
    soup = bs4.BeautifulSoup(content, "lxml")
    return soup.find_all('div', {"class": "c-item_footer"})

def format_news():
    news_tags = get_news()

    result = ""

    for news in news_tags:
        result += news.text + "\n"

    return result


