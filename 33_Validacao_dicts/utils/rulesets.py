from datetime import date

class Rulesets:
    """Classe """

    today = date.today()
    anomesdia = today.strftime("%Y%m%d")

    @staticmethod
    def obter_regra(nome_regra: str) -> dict:
        """Obtém a regra de ruleset com base no nome fornecido.
        Args:
            nome_regra (str): Nome da regra de ruleset a ser obtida.
        Returns:
            dict: Dicionário contendo os detalhes da regra de ruleset.
        """

        return Rulesets.__dict__[nome_regra]
    
    primeira_regra = {
        "rules": {
            "id": 1,
            "nome": "Regra de Teste 01",
            "descricao": "Esta é a primeira regra criada.",
            "data_criacao": anomesdia,
            "ativo": True
        }
    }

    segunda_regra = {
        "rules": {
            "id": 2,
            "nome": "Regra de Teste 02",
            "descricao": "Esta é a segunda regra criada.",
            "data_criacao": anomesdia,
            "ativo": False
        }
    }
