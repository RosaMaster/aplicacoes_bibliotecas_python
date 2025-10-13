import requests
from list_dict import ListaDict

lista_dict = ListaDict()

lista_api = [
    "consulta_types",
    "consulta_pokemon"
]


for dicionario in lista_api:

    consulta = lista_dict.get_dict(getattr(lista_dict, dicionario))

    #print(consulta)

    response = requests.request(consulta["METHOD"], consulta["URL"], data=consulta["PAYLOAD"], headers=consulta["HEADERS"])

    #print(response.status_code)
    #print(response.text)

    if response.status_code == 200:
        print(f"✅ {consulta['API_NAME']} | ENV: {consulta['ENV']} | STATUS: {response.status_code}")
    
    else:
        print(f"❌ {consulta['API_NAME']} | ENV: {consulta['ENV']} | STATUS: {response.status_code}")
