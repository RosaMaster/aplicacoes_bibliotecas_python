### Gerador UUID

**UUID (Universally Unique Identifier)** é um identificador único universalmente utilizado para identificar informações em sistemas distribuídos sem a necessidade de uma autoridade central. Ele é amplamente utilizado em várias aplicações, como bancos de dados, sistemas distribuídos e APIs, para garantir que cada identificador seja único.

<br>

| **Documentação**                                                                                |
| ----------------------------------------------------------------------------------------------- |
| [docs.python.org](https://docs.python.org/3.14/library/uuid.html)                               |
| [stackoverflow](https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python) |

<br>

| **UUID** | **DESCRIÇÃO**                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------- |
| UUID1    | Baseado no tempo e no endereço MAC do computador. Pode ser usado para garantir a unicidade em um ambiente distribuído |
| UUID3    | Baseado no hash MD5 de um namespace e um nome. Útil para gerar UUIDs determinísticos                                  |
| UUID4    | Gerado aleatoriamente. É o tipo mais comum e amplamente utilizado                                                     |
| UUID5    | Baseado no hash SHA-1 de um namespace e um nome. Similar ao UUID3, mas usa SHA-1 em vez de MD5                        |


`O UUID2 não é amplamente suportado na biblioteca padrão uuid de Python, pois ele é específico para algumas implementações de sistemas e não é parte do padrão RFC 4122. No entanto, você pode usar os outros tipos de UUID (UUID1, UUID3, UUID4, UUID5) que são amplamente suportados e padronizados`


#### Diferenças entre as versões do UUID

**UUID1:**<br>

- Baseado no tempo: Gera um UUID usando o timestamp atual e o endereço MAC do computador.
- Uso: Pode ser usado para garantir a unicidade em um ambiente distribuído.
- Exemplo: 6fa459ea-ee8a-11d2-9a0c-4a6f7b7c5e5f<br><br>

**UUID2:**<br>

- Baseado no tempo e identificador local: Não é amplamente suportado na biblioteca padrão uuid de Python.
- Uso: Específico para algumas implementações de sistemas.
- Exemplo: Não suportado pelo módulo uuid em Python.<br><br>

**UUID3:**<br>

- Baseado no hash MD5: Gera um UUID usando o hash MD5 de um namespace e um nome.
- Uso: Útil para gerar UUIDs determinísticos.
- Exemplo: 9073926b-929f-31c2-abc9-fad77ae3e8eb<br><br>

**UUID4:**<br>

- Gerado aleatoriamente: Gera um UUID usando números aleatórios.
- Uso: É o tipo mais comum e amplamente utilizado.
- Exemplo: 16fd2706-8baf-433b-82eb-8c7fada847da<br><br>

**UUID5:**<br>

- Baseado no hash SHA-1: Gera um UUID usando o hash SHA-1 de um namespace e um nome.
- Uso: Similar ao UUID3, mas usa SHA-1 em vez de MD5.
- Exemplo: 21f7f8de-8051-5b89-8680-0195ef798b6a


#### Exemplo de Código

Aqui está um exemplo de como gerar diferentes tipos de UUIDs em Python usando o módulo uuid:

~~~Python
import uuid

# Gerar um UUID baseado no tempo (UUID1)
uuid1 = uuid.uuid1()
print(f"UUID1: {uuid1}")

# Gerar um UUID baseado no nome e namespace (UUID3, usando MD5)
uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
print(f"UUID3: {uuid3}")

# Gerar um UUID aleatório (UUID4)
uuid4 = uuid.uuid4()
print(f"UUID4: {uuid4}")

# Gerar um UUID baseado no nome e namespace (UUID5, usando SHA-1)
uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
print(f"UUID5: {uuid5}")
~~~

##### Conclusão

A geração de UUIDs em Python é simples e pode ser feita usando o módulo uuid da biblioteca padrão. Dependendo do caso de uso, você pode escolher entre diferentes tipos de UUIDs para garantir a unicidade dos identificadores