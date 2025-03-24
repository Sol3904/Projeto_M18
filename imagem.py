from PIL import Image, ImageEnhance, ImageColor, ImageFile, ImageFilter
ImageFile.LOAD_TRUNCATED_IMAGES = True

img = Image.open(r"C:\\Users\\solan\\Downloads\\aigischibi.jpg")
aigis = ImageEnhance.Sharpness(img).enhance(5.0)
aigis = ImageEnhance.Brightness(img).enhance(5.0)
aigis = ImageEnhance.Contrast(img).enhance(5.0)
aigis = ImageEnhance.Color(img).enhance(5.0)

aigis_contorno = aigis.filter(ImageFilter.CONTOUR)

cor_rgb = ImageColor.getrgb("blue")  # Retorna (0, 0, 255)
cor_rgb2 = ImageColor.getrgb("#FF5733")  # Retorna (255, 87, 51)

print(cor_rgb, cor_rgb2)

aigis_contorno.show()
