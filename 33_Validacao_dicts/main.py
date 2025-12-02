from utils.rulesets import Rulesets
from test.payload_rulesets import PayloadRulesets

def main():

    lista_de_regras = [
        "primeira_regra",
        "segunda_regra"
    ]


    for nome_regra in lista_de_regras:
        ruleset = Rulesets.obter_regra(nome_regra)
        payload = PayloadRulesets.obter_regra(nome_regra)
        assert ruleset == payload, f"❌ Regras não coincidem para {nome_regra}!"
        print(f"✅ Regras coincidem para {nome_regra}.")
        print(type(ruleset))
        print(ruleset.get("rules")["id"])
        print(type(payload))
        print(payload.get("rules")["nome"])

    

if __name__ == "__main__":
    main()
