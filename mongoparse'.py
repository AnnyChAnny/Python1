from mongoengine import *

connect('parcing')
import requests
import bs4

class User(Document):
    link = StringField(required=True)
    title = StringField(max_length=500)
    text = StringField()



response = requests.get('https://osvita.ua/')
# print(response.text)


html_page = bs4.BeautifulSoup(response.text, "html.parser")
all_a = html_page.find_all("a")
list_clean_href = []
for a in all_a:

    href = a.get('href')
    # print(href)

    if href not in list_clean_href and not "http" in href:
        title = a.get('title')
        # if not title:
        #     continue
        href="https://osvita.ua"+ href
        list_clean_href.append(href)

        response_text = requests.get(href)
        html_page_article = bs4.BeautifulSoup(response_text.text, "html.parser")
        text_article_block = html_page_article.find('div', {"class": "article"})
        if not text_article_block:
            continue
        text = ""
        for p in text_article_block.find_all("p"):
            text += p.get_text()
        database=User(link=href,title=title,text=text)
        database.save()
