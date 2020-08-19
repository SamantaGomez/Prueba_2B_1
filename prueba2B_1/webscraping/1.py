import requests
from bs4 import BeautifulSoup
# Import MongoClient from pymongo so we can connect to the database
from pymongo import MongoClient

if _name_ == '_main_':

    db_client = MongoClient()
    bdd3 = db_client.bdd3
    bdd3 = bdd3.posts

    response = requests.get("https://eckomusic.com")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("a", class_="product-name")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title.text,
            'link'  : "https://eckomusic.com" + post_title['href']
        })

    for post in extracted:
        if db_client.bdd3.bdd3.find_one({'link': post['link']}) is None:
            print("Found a new listing at the following url: ", post['link'])
            db_client.bdd3.bdd3.insert(post)