import pandas as pd
import numpy as np

# Dados de exemplo
data = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [23, 45, 36, 29],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
}

# Criação do DataFrame
df = pd.DataFrame(data)

print(df)