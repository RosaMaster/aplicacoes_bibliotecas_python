from random import choice, randint, shuffle

# List of letters, numbers and symbols
letrasAlfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Laço para gerar a senha de forma aleatória
password_letters = [choice(letrasAlfabeto) for _ in range(randint(8, 10))]
password_symbols = [choice(simbolos) for _ in range(randint(2, 4))]
password_numbers = [choice(numeros) for _ in range(randint(2, 4))]

# Printando as listas e seus tamanhos
print(password_letters)
print(len(password_letters))
print(password_symbols)
print(len(password_symbols))
print(password_numbers)
print(len(password_numbers))

# Concatenando as listas
password_list = password_letters + password_symbols + password_numbers
# print(password_list)

# Embaralhando a lista
shuffle(password_list)
# print(password_list)

# Convertendo a lista em string
password_list = "".join(password_list)
print(f"Your password is: {password_list}")

