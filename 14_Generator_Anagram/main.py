name_input = "Angela Rosa de Oliveira"
print(name_input)
name_input = name_input.upper()

list_name = name_input.split()
print(list_name)

# list comprehension
criar_nome = [nome for nome in list_name if len(nome) > 3]
print(criar_nome)
if len(criar_nome) < 7:
    primeiras_letras = [nome[:2] for nome in criar_nome]
    if len(primeiras_letras) < 7:
        primeiras_letras = [nome[:3] for nome in criar_nome]

else:
    primeiras_letras = [nome[0] for nome in criar_nome]

print(primeiras_letras)
racf = "".join(primeiras_letras)
print(racf)