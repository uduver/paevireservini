from datetime import date
import download_background

def main():
    download_background.download_image(download_background.get_random_image_url(date.today()), f"resources/backgrounds/{date.today()}.jpg")

main()