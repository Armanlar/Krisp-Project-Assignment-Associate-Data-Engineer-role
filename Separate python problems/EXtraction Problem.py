
############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############
import requests
from bs4 import BeautifulSoup
google_news_url="https://news.google.com/news/rss"

def get_headlines(rss_url):
    response = requests.get(rss_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, features="xml")
    titles = soup.find_all('title') 
    for title in titles:
        print(title.string)
print(get_headlines(google_news_url))

