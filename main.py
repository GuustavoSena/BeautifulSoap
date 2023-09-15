from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-46435'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

box_article = soup.find('article', class_='main-article')

movie_title = box_article.find('h1').get_text()