from PIL import Image, ImageEnhance, ImageFilter

def enhance_image(image_path):
    """Apply automatic enhancements to the uploaded image."""
    try:
        img = Image.open(image_path)

        # Apply enhancements
        img = ImageEnhance.Sharpness(img).enhance(2.0)  # Increase sharpness
        img = ImageEnhance.Brightness(img).enhance(1.5)  # Increase brightness
        img = ImageEnhance.Contrast(img).enhance(1.5)  # Increase contrast
        img = ImageEnhance.Color(img).enhance(1.5)  # Boost colors

        # Apply a slight edge enhancement filter
        img = img.filter(ImageFilter.EDGE_ENHANCE)

        # Save the modified image
        img.save(image_path)
        print(f"Enhanced image saved: {image_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
