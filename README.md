# Projeto de Aprendizado - Web Scraping com BeautifulSoup

Este é um projeto de aprendizado que demonstra a técnica de Web Scraping usando a biblioteca BeautifulSoup em Python. O objetivo deste projeto é coletar transcrições de filmes do site "subslikescript.com" para fins de aprendizado.

## Funcionalidade

O script Python neste projeto, localizado no arquivo `main.py`, realiza as seguintes tarefas:

1. Acessa a página inicial do site "subslikescript.com" e coleta informações sobre a paginação.
2. Cria uma pasta principal chamada "movie_transcriptions" no diretório atual, onde as transcrições de filmes serão armazenadas.
3. Itera pelas páginas de paginação, criando uma subpasta para cada página.
4. Coleta links para as transcrições de filmes em cada página.
5. Acessa as páginas individuais de transcrições de filmes, extrai o título do filme e a transcrição.
6. Salva a transcrição em um arquivo de texto (.txt) dentro da subpasta correspondente.

## Uso

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o script:

- BeautifulSoup
- requests

Para executar o script, simplesmente execute o arquivo Python `main.py` no seu ambiente Python.

```bash
python main.py
