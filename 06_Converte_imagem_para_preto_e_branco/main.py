# Convertendo imagens para imagem preto e branco

from PIL import Image
from DATA.lista_imagem import lista_imagem

for i in range(len(lista_imagem)):

    # Abre a imagem
    img = Image.open(f'img\\{lista_imagem[i]}')

    # Converte a imagem para preto e branco
    img = img.convert('L')

    # Salva a imagem
    img.save(f'img/img_0{i + 1}_bw.jpg')

