import requests
from bs4 import BeautifulSoup


url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')


for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    print(data.text, titulo.text, sep='\t')

