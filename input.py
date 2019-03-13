import os
import json

path = os.path.dirname(os.path.abspath(__file__))
data = {}

data['name'] = input('Informe o seu nome: ')
data['age'] = int(input('Informe a sua idade: '))
data['city'] = input('Informe a sua cidade: ')

with open(f'{path}/data.json', 'w') as outfile:
    json.dump(data, outfile)
