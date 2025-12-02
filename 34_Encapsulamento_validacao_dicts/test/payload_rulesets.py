from datetime import date
import copy

class Rulesets:

    _today = date.today()
    _anomesdia = _today.strftime("%Y%m%d")

    # armazenamento privado de regras
    _rules = {
        "primeira_regra": {
            "rules": {
                "id": 1,
                "nome": "Regra de Teste 01",
                "descricao": "Esta é a primeira regra criada.",
                "data_criacao": _anomesdia,
                "ativo": True
            }
        },
        "segunda_regra": {
            "rules": {
                "id": 2,
                "nome": "Regra de Teste 02",
                "descricao": "Esta é a segunda regra criada.",
                "data_criacao": _anomesdia,
                "ativo": False
            }
        }
    }

    @classmethod
    def obter_regra(cls, nome_regra: str) -> dict:
        """Retorna uma cópia da regra para evitar mutação externa."""
        
        try:
            return copy.deepcopy(cls._rules[nome_regra])
        except KeyError:
            raise KeyError(f"Regra '{nome_regra}' não encontrada")