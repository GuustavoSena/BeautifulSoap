from bs4 import BeautifulSoup
import requests
import os

ROOT_WEBSITE = 'https://subslikescript.com/'
WEBSITE = f'{ROOT_WEBSITE}movies_letter-A'
result = requests.get(WEBSITE, timeout=10)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Pagination
box_pagination = soup.find('ul', class_='pagination')
pages = box_pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

# Pasta de transcrições de filmes
main_output_folder = os.path.join(os.getcwd(), 'movie_transcriptions')
os.makedirs(main_output_folder, exist_ok=True)

for num_page in range(1, int(last_page) + 1)[:3]:
    # Criar uma pasta para cada página de paginação
    page_output_folder = os.path.join(main_output_folder, f'page_{num_page}')
    os.makedirs(page_output_folder, exist_ok=True)

    result = requests.get(f'{WEBSITE}?page={num_page}', timeout=10)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box_article = soup.find('article', class_='main-article')

    links = []

    for link in box_article.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            print(link)
            result = requests.get(f'{ROOT_WEBSITE}{link}', timeout=10)
            content = result.text

            soup = BeautifulSoup(content, 'lxml')

            box_article = soup.find('article', class_='main-article')

            movie_title = box_article.find('h1').get_text()
            transcription = box_article.find(
                'div', class_='full-script').get_text(strip=True, separator=' ')

            # Salvar o arquivo .txt dentro da pasta da página correspondente
            with open(os.path.join(page_output_folder, f'{movie_title}.txt'), 'w', encoding="utf-8") as file:
                file.write(transcription)
        except requests.exceptions.RequestException as e:
            print(f"Erro de solicitação HTTP: {e}")
            print(link)
        except Exception as e:
            print(f"Erro não esperado: {e}")
