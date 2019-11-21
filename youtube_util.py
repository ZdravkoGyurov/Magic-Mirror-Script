import urllib.request
from bs4 import BeautifulSoup
import webbrowser

def play_video(text_to_search):
  query = urllib.parse.quote(text_to_search)
  url = "https://www.youtube.com/results?search_query=" + query
  response = urllib.request.urlopen(url)
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')
  
  for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
    webbrowser.open("https://www.youtube.com" + vid["href"])
    return
