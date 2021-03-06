'''
Cotação do Dolar usando API
É possivel definir um gatilho para compra da moeda, assim o programa te avisa
É preciso instalar o programa: Speed Dispatcher, use o comando: sudo apt-get install speech-dispatcher
Por: Ricardo Rocha
deltab@gmail.com
'''

import requests
import json
import time
import os
import re

def limpa_tela():
    os.system('clear')

def menu_principal():
    print('=============================')
    print('SENHOR DOLAR v.1.0')
    print('=============================')

    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
    requisicao = requests.get(url)
    resposta = json.loads(requisicao.text)

    horario = resposta['USD']['create_date']
    converte = re.search(r'.\w:\w+...', horario)

    print(resposta['USD']['name'])
    print('Preço de Compra....:', 'R$', resposta['USD']['bid'])
    print('Preço de Venda.....:', 'R$', resposta['USD']['ask'])
    print('Última Atualização.:', converte.group())
    print('')
    print('Atualização a cada 30 segundos...')

    if resposta['USD']['bid'] >= pergunta:
        os.system('spd-say comprar-comprar-comprar')
        time.sleep(5)
        print('Saindo...')
        time.sleep(5)
        exit(0)
    else:
        time.sleep(30)
        limpa_tela()

print('')
pergunta = input('Em qual valor deseja comprar? ')
print('')

while True:
    menu_principal()
