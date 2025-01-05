import httpx
from utils.lista_moedas import moedas


# IMPRIME AS MOEDAS DISPONÍVEIS
print(f"{moedas}\n")


# SOLICITA A MOEDA DE BASE E A MOEDA DESEJADA
base_currency = input("Digite a moeda de base: ").upper()   # USD
currency = input("Digite a moeda desejada: ").upper()       # BRL


# BUSCA VALORES DE MOEDAS NA API PRIVADA
response = httpx.get(
    url=f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
).json()


# EXIBE O VALOR DA MOEDA DESEJADA
currency_data = response.get('rates').get(currency)

print(f'1 {base_currency} vale {currency_data} {currency}')

