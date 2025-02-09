### Manipulação de JSON em Python

#### Introdução

JSON (JavaScript Object Notation) é um formato leve de intercâmbio de dados que é fácil para os humanos lerem e escreverem, e fácil para as máquinas analisarem e gerarem. Em Python, a manipulação de JSON é feita principalmente usando o módulo `json`.

<br>

| **Documentação**                                               |
| -------------------------------------------------------------- |
| [docs.python.org](https://docs.python.org/3/library/json.html) |

#### Leitura de Arquivos JSON

Para ler um arquivo JSON em Python, você pode usar a função `json.load()`. Aqui está um exemplo:

~~~~python
import json

# Ler o arquivo JSON
with open('caminho/para/seu/arquivo.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
~~~~


#### Escrita em Arquivos JSON

Para escrever dados em um arquivo JSON, você pode usar a função json.dump(). Aqui está um exemplo:

~~~~python
import json

dados = {
    "nome": "Joao",
    "idade": 30,
    "cidade": "São Paulo"
}

# Escrever em um arquivo JSON
with open('caminho/para/seu/arquivo.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)
~~~~


#### Manipulação de Dados JSON

##### Adicionar Campos

Para adicionar um novo campo a um dicionário JSON, você pode simplesmente atribuir um valor a uma nova chave:

~~~~python
dados['email'] = 'joao@example.com'
~~~~


#### Remover Campos

Para remover um campo de um dicionário JSON, você pode usar a palavra-chave del:

~~~~python
del dados['idade']
~~~~


#### Atualizar Campos

Para atualizar um campo existente, você pode atribuir um novo valor à chave existente:

~~~~python
dados['cidade'] = 'Rio de Janeiro'
~~~~


#### Exemplo Completo

Aqui está um exemplo completo que lê um arquivo JSON, modifica os dados e grava em um novo arquivo JSON:

~~~~python
import json

def main():
    # Ler o arquivo JSON
    with open('cliente.json', 'r') as arquivo_read:
        dados = json.load(arquivo_read)

    # Modificar os dados
    dados['sexo'] = 'M'
    dados['idade'] = 25
    nova_vistoria = {'data': '20200522', 'local': 'SHOPING', 'resultado': 'Aprovado'}
    if 'vistorias' in dados['carro']:
        dados['carro']['vistorias'].append(nova_vistoria)
    else:
        dados['carro']['vistorias'] = [nova_vistoria]

    # Remover campos
    del dados['email']
    del dados['idiomas']
    del dados['carro']
    del dados['sexo']

    # Gravar em um novo arquivo JSON
    with open('cliente_v3.json', 'w') as arquivo_write:
        json.dump(dados, arquivo_write, indent=4)

if __name__ == '__main__':
    main()
~~~~


##### Conclusão

A manipulação de JSON em Python é uma tarefa comum e essencial para muitas aplicações. Usando o módulo json, você pode facilmente ler, escrever e modificar dados JSON de maneira eficiente e eficaz.<br><br>

[**HOME**](#manipulação-de-json-em-python)