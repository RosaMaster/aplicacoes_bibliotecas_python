from utils.utils import NumberToWords

# Input dado pelo usuário
numero = int(input('Digite um número: '))

# Instanciando a classe NumberToWords
num_en = NumberToWords.convert_to_english(numero)                   # Chamando o método convert_to_english
print(f'Em Inglês: {num_en}')

num_en_ord = NumberToWords.convert_to_ordinal(numero)               # Chamando o método convert_to_ordinal
print(f'Em Inglês (ordinal): {num_en_ord}')

num_pt = NumberToWords.convert_to_portuguese(numero)                # Chamando o método convert_to_portuguese
print(f'Em Português: {num_pt}')

num_pt_ord = NumberToWords.convert_to_portuguese_ordinal(numero)    # Chamando o método convert_to_portuguese_ordinal
print(f'Em Português (ordinal): {num_pt_ord}')
