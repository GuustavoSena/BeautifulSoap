from bs4 import BeautifulSoup
import requests
import os

ROOT_WEBSITE = 'https://subslikescript.com/'
WEBSITE = f'{ROOT_WEBSITE}movies'
result = requests.get(WEBSITE, timeout=10)
content = result.text

soup = BeautifulSoup(content, 'lxml')

box_article = soup.find('article', class_='main-article')

links = []
for link in box_article.find_all('a', href=True):
    links.append(link['href'])

output_folder = os.path.join(os.getcwd(), 'movie_transcriptions')
os.makedirs(output_folder, exist_ok=True)

for link in links:
    SPECIFIC_MOVIE_WEBSITE = f'{ROOT_WEBSITE}{link}'
    result = requests.get(SPECIFIC_MOVIE_WEBSITE, timeout=10)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    box_article = soup.find('article', class_='main-article')

    movie_title = box_article.find('h1').get_text()
    transcription = box_article.find(
        'div', class_='full-script').get_text(strip=True, separator=' ')

    with open(os.path.join(output_folder, f'{movie_title}.txt'), 'w', encoding="utf-8") as file:
        file.write(transcription)
