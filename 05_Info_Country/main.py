from countryinfo import CountryInfo
from DATA.list_country_names import country_name

print(f"{country_name}\n")

country = CountryInfo(input('Digite o nome do país: '))

print(f'País: {country.name()}')
print(f'Capital: {country.capital()}')
print(f'Moedas: {country.currencies()}')
print(f'Idiomas: {country.languages()}')
print(f'Fazem fronteira: {country.borders()}')
print(f'Código de área: {country.calling_codes()}')
print(f'População: {country.population()}')

