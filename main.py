from datetime import date
import download_background
import generate_image

def main():

    background_path: str = f"resources/backgrounds/{date.today()}.jpg"
    download_background.download_image(background_path)
    instagram_post = generate_image.create_image(65, background_path)
    instagram_post.save(f"output/{date.today()}.jpg", "JPEG", quality=100)


main()