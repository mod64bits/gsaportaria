from PIL import Image


def inserir_logo(img):
    logo = Image.open("logo-removebg.png").convert("RGBA")
    logo.show()
    imagem = Image.open(img).convert("RGBA")
    imagem.show()
    resized_logo = logo.resize((round(300), round(300)))
    resized_imagem = imagem.resize((round(1200), round(695)))
    resized_imagem.paste(resized_logo, (900, 350), mask=resized_logo)
    resized_imagem.save(img)
