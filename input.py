import os
import json

path = os.path.dirname(os.path.abspath(__file__))
informacoes = {}

informacoes['nome'] = input('Informe o seu nome: ')
informacoes['idade'] = int(input('Informe a sua idade: '))
informacoes['cidade'] = input('Informe a sua cidade: ')

with open(f'{path}/data.json', 'w') as outfile:
    json.dump(informacoes, outfile)
