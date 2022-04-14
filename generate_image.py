from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

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

def add_text_to_image(image: Image, days_left: str):
    # Add text to the background image
    draw = ImageDraw.Draw(image)

    # Big font used for days.
    font_header = ImageFont.truetype("resources/fonts/Poppins-Black.ttf", size=300)
    # Font for the percentage.
    font_text = ImageFont.truetype(
        "resources/fonts/Poppins-Bold.ttf", size=48)
    
    # Draw percentage text
    draw.text((1080/2, 930), f"{round(((335-days_left)/335)*100, 2)}%", (255, 255, 255), font=font_text, anchor="mm")

    # Draw days left text
    draw.text((1080/2, 1080/2), f"{days_left}", (255, 255, 255), font=font_header, anchor="mm")

    return image

def create_image(days_left: int):
    background_image = create_background_image("resources/backgrounds/2022-04-13.jpg")
    instagram_post = add_progress_bar(background_image, days_left)
    instagram_post = add_text_to_image(instagram_post, days_left)

    return instagram_post

# Source: https://stackoverflow.com/a/66887674
def draw_progress_bar(d, x, y, w, h, progress, bg=(255, 255, 255, 128), fg=(23, 87, 174)):
    # draw background
    d.ellipse((x+w, y, x+h+w, y+h), fill=bg)
    d.ellipse((x, y, x+h, y+h), fill=bg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

    # draw progress bar
    w *= progress
    d.ellipse((x+w, y, x+h+w, y+h), fill=fg)
    d.ellipse((x, y, x+h, y+h), fill=fg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=fg)

    return d

def add_progress_bar(image, days_left):
    # create image or load your existing image with out=Image.open(path)
    draw = ImageDraw.Draw(image)
    # draw the progress bar to given location, width, progress and color
    draw = draw_progress_bar(draw, 100, 880, 780, 100, (335-days_left)/335)
    return image

create_image(65).show()