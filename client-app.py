import requests
import random

endpoints = ['renda-fixa', 'renda-variavel', 'fii', 'cripto']
seguir_rodando = True

while seguir_rodando:
    requisicao = requests.get(f'http://app:5000/{random.choice(endpoints)}') #deu erro
    # requisicao_daniel = requests.get('http://app:5000/'+endpoints[random.randint(0,3)])
