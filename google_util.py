import urllib.request
from bs4 import BeautifulSoup

def get_news():
  news_url = "https://news.google.com/?hl=bg&gl=BG&ceid=BG:bg"
  #news_url = "https://news.google.com/news"
  response = urllib.request.urlopen(news_url)
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')
  
  file = open("news_report.txt", "w+")
  
  i = 1
  max_article_text = 50
  max_articles = 15
  for article in soup.select('h3 > a'):
    if i > max_articles:
        break
    if(len(article.text) > max_article_text):
        file.write(str(i) + ". " + article.text[0:max_article_text] + "...\n")
    else:
        file.write(str(i) + '. ' + article.text + "\n")
    i += 1
    
  file.close()

get_news()
