from rembg import remove
from PIL import Image

# Importa a imagem original
img = Image.open('img/ds.jpeg')
                 
#Remove o fundo da imagem
img_without_back = remove(img)

# Salva a imagem sem fundo
img_without_back.save('ds_without_back.png')

print("Imagem salva com sucesso!")

