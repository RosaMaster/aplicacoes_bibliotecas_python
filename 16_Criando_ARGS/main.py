import pandas as pd
from unittest.mock import patch
import argparse

# Suponha que você tenha o seguinte DataFrame
df = pd.DataFrame({
    'Nome': ['João'],
    'Idade': [25],
    'Cidade': ['São Paulo']
})

# Converta o DataFrame em um dicionário
data_dict = df.to_dict('records')[0]

# Cria o parser
parser = argparse.ArgumentParser(description="Processa os dados de entrada.")

# Adiciona os argumentos
parser.add_argument('--Nome', type=str, required=True, help='Nome do usuário')
parser.add_argument('--Idade', type=int, required=True, help='Idade do usuário')
parser.add_argument('--Cidade', type=str, required=True, help='Cidade do usuário')

# Use os valores do dicionário como argumentos
args = parser.parse_args(['--Nome', data_dict['Nome'], '--Idade', str(data_dict['Idade']), '--Cidade', data_dict['Cidade']])

# Agora você pode usar args.Nome, args.Idade e args.Cidade em seu código
print(f'Nome: {args.Nome}, Idade: {args.Idade}, Cidade: {args.Cidade}')

# Cria um mock dos argumentos
with patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(Nome='Edu', Idade=32, Cidade='Parana')):
    args = parser.parse_args()

print(f'Nome: {args.Nome}, Idade: {args.Idade}, Cidade: {args.Cidade}')