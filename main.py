from bs4 import BeautifulSoup
import requests

WEBSITE = 'https://subslikescript.com/movie/Titanic-46435'
result = requests.get(WEBSITE)
content = result.text

soup = BeautifulSoup(content, 'lxml')

box_article = soup.find('article', class_='main-article')

movie_title = box_article.find('h1').get_text()

transcription = box_article.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{movie_title}.txt', 'w', encoding="utf-8") as file:
    file.write(transcription)
