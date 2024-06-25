from rembg import remove 
from PIL import Image
from DATA.lista_imagem import lista_imagem

# Remove o fundo de todas as imagens
for i in range(len(lista_imagem)):

    # Abre a imagem
    img = Image.open(f'img/{lista_imagem[i]}')

    # Remove o fundo da imagem
    img_without_back = remove(img)

    # Salva a imagem sem fundo
    img_without_back.save(f'img/img_0{i + 1}_without_back.jpg')

