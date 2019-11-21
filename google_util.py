import urllib.request
from bs4 import BeautifulSoup

def get_news():
  news_url = "https://news.google.com/?hl=bg&gl=BG&ceid=BG:bg"
  #news_url = "https://news.google.com/news"
  response = urllib.request.urlopen(news_url)
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')
  
  i = 1
  for article in soup.select('h3 > a'):
    print(str(i) + ". " + article.text)
    i += 1
