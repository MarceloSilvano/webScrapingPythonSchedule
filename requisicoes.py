import requests
from bs4 import BeautifulSoup

# Faz o request para a URL
url = 'https://ge.globo.com/futebol/brasileirao-serie-a/'
response = requests.get(url)

# Parseia o conteúdo HTML usando BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra a tabela de classificação com base na classe
tabela = soup.find('div', {'class': 'column small-24 medium-centered medium-20 large-22 tabela-body'})
tabela = soup.find('script', {'id': 'scriptReact'})



