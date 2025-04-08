from PIL import Image, ImageEnhance, ImageFilter

# Aplica alterações na imagem.
def enhance_image(image_path, sharpness=1.0, brightness=1.0, contrast=1.0, color=1.0):
    try:
        img = Image.open(image_path)
        img = ImageEnhance.Sharpness(img).enhance(sharpness)
        img = ImageEnhance.Brightness(img).enhance(brightness)
        img = ImageEnhance.Contrast(img).enhance(contrast)
        img = ImageEnhance.Color(img).enhance(color)

        img.save(image_path)  # Salva a imagem editada
        print(f"Imagem editada salva: {image_path}")
    except Exception as e:
        print(f"Erro ao processar imagem {image_path}: {e}")

