

class ListaDict:

    # Criar função que retornará o dicionario de dados
    def get_dict(self, dictionary):
        
        return dictionary


    consulta_types = {
        "METHOD": "GET",
        "URL": "https://loteriascaixa-api.herokuapp.com/api/",
        "PAYLOAD": "",
        "HEADERS": {"User-Agent": "insomnia/10.1.1"},
        "API_NAME": "loterias",
        "ENV": "PROD"
    }

    consulta_pokemon = {
        "METHOD": "GET",
        "URL": "https://pokeapi.co/api/v2/pokemon/ditto",
        "PAYLOAD": "",
        "HEADERS": {"User-Agent": "insomnia/10.1.1"},
        "API_NAME": "pokemon ",
        "ENV": "PROD"
    }
