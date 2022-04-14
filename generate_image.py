from PIL import Image, ImageOps, ImageFilter

def create_background_image(background_image_path: str):
    background_image = Image.open(background_image_path)

    # Crop and resize the image to 1080p for Instagram
    background_image = ImageOps.fit(background_image, (1080, 1080), bleed=0.0, centering=(0.5, 0.5))

    # Add gaussian blur to the background image
    background_image = background_image.filter(ImageFilter.GaussianBlur(radius=2))

    # Add overlay to the background image. Contains the necessary text and gradient to the image.
    overlay_image = Image.open("resources/overlay.png")
    background_image.paste(overlay_image, (0, 0), overlay_image)

    return background_image
