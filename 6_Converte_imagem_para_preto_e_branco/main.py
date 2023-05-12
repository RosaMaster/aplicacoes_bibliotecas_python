# Convertendo imagens para imagem preto e branco

from PIL import Image

# Carrega Imagem
image_file = Image.open("colorida.png")


# Converte imagem para preto e branco
image_file = image_file.convert("L")


# Salva imagem em preto e branco
image_file.save("preto_branco.png")

