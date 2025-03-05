### Utilizando Boto3 e Pytest para validar serviços AWS

**boto3** é o SDK (Software Development Kit) da AWS (Amazon Web Services) para a linguagem de programação Python. Em termos simples, ele é uma biblioteca que permite que desenvolvedores Python interajam com os serviços da AWS de forma programática
<br>

**pytest** é um framework de testes para Python que torna simples escrever e executar testes. Ele é amplamente utilizado devido à sua sintaxe concisa, recursos poderosos e extensibilidade

<br>

| **Documentação**                                                              |
| ----------------------------------------------------------------------------- |
| [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)   |
| [pytest](https://docs.pytest.org/en/stable/getting-started.html)              |


#### Install lib's

~~~Python
pip install boto3
~~~

~~~Python
pip install -U pytest
~~~


#### BOTO3 `INFO`

<details>

##### Principais características e funcionalidades:

- Facilidade de uso: Boto3 simplifica a interação com os serviços da AWS, fornecendo uma interface Python amigável
- Ampla cobertura de serviços: Ele oferece suporte a uma vasta gama de serviços da AWS, incluindo:

|                                       |
| ------------------------------------- |
| Amazon S3 (armazenamento de objetos)  |
| Amazon EC2 (computação em nuvem)      |
| AWS Lambda (computação sem servidor)  |
| Amazon DynamoDB (banco de dados NoSQL)|

E muitos outros

- Automação de tarefas: Com Boto3, é possível automatizar tarefas complexas na AWS, como:

|                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- |
| Criar e gerenciar instâncias EC2                                                                                      |
| Fazer upload e download de arquivos para o S3                                                                         |
| Executar funções Lambda                                                                                               |
| Consultar e manipular dados no DynamoDB                                                                               |
| Desenvolvimento de aplicações: Boto3 é essencial para o desenvolvimento de aplicações que utilizam os serviços da AWS |


##### Em resumo:

Boto3 é uma ferramenta poderosa para desenvolvedores Python que desejam aproveitar os recursos da AWS. Ele permite que você integre seus aplicativos e scripts Python com a infraestrutura da AWS, automatizando tarefas e criando soluções escaláveis

</details>


#### PYTEST `INFO`

<details>

##### Principais características:

###### Simplicidade

- Permite escrever testes de forma clara e direta, com menos código boilerplate em comparação com outros frameworks
- A sintaxe é intuitiva, facilitando o aprendizado e uso
- Detecção automática de testes:

|                                                                                                           |
| --------------------------------------------------------------------------------------------------------- |
| Pytest detecta automaticamente arquivos e funções de teste seguindo convenções de nomenclatura simples    |
| Isso simplifica a execução de testes, pois não é necessário especificar manualmente quais testes executar |

- Fixtures:

|                                                                                                           |
| --------------------------------------------------------------------------------------------------------- |
| Fixtures são funções que configuram o ambiente de teste e fornecem dados ou recursos para os testes       |
| Elas permitem reutilizar código de configuração e simplificar a escrita de testes                         |

- Plugins:

|                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------- |
| Pytest possui uma vasta coleção de plugins que estendem suas funcionalidades                                        |
| Plugins podem adicionar recursos como cobertura de código, testes de desempenho e integração com outras ferramentas |

- Relatórios detalhados:

|                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- |
| Pytest gera relatórios de teste detalhados, facilitando a identificação de falhas e o diagnóstico de problemas |
| Os relatórios incluem informações sobre quais testes passaram, falharam ou foram ignorados                     |

##### Por que usar Pytest?

- Produtividade

Pytest agiliza o processo de teste, permitindo que os desenvolvedores escrevam e executem testes com mais rapidez

- Qualidade do código

Ao facilitar a escrita de testes, Pytest incentiva a prática de testes unitários e de integração, contribuindo para a qualidade do código.

- Manutenção

Fixtures e plugins tornam os testes mais organizados e fáceis de manter

- Comunidade

Pytest possui uma comunidade ativa e uma vasta documentação, o que facilita a obtenção de ajuda e suporte

Em resumo, Pytest é uma ferramenta poderosa e flexível que simplifica o processo de teste em Python, ajudando os desenvolvedores a escrever código de alta qualidade

</details>
