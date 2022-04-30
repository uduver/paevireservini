from datetime import date, datetime
from functions import download_background, generate_image, upload_to_instagram
import time
import os

def main():
    days_left: int = (date(2022, 6, 17) - date.today()).days

    background_path: str = f"resources/backgrounds/{date.today()}.jpg"
    # When the background download fails use a backup image.
    try:
        download_background.download_image(background_path)
    except print(0):
        background_path: str = f"resources/backgrounds/backup.jpg"

    download_background.download_image(background_path)
    instagram_post_image = generate_image.create_image(days_left, background_path)
    instagram_post_image.save(f"output/{date.today()}.jpg", "JPEG", quality=100)

    instagram = upload_to_instagram.Instagram(
        os.getenv('API_ACCESS_TOKEN'),  os.getenv('API_CLIENT_ID'), os.getenv('API_CLIENT_SECRET'), os.getenv('INSTAGRAM_PAGE_ID'))

    instagram_post_id = instagram.single_media_post(
        f"\U0001F3E0 Reservini on jäänud {days_left} päeva.\n\U0001F3C6 {round(((335-days_left)*100/335), 1)}% ajateenistusest on läbitud.", f"http://{os.getenv('PUBLIC_IP')}:8080/{date.today()}.jpg")


    instagram.publish_container(instagram_post_id)
    instagram.refresh_token()
    
    return


while True:
    # Stupid way to make sure the program runs every day.
    if datetime.now().hour == 0 and datetime.now().minute == 25:
        main()
        time.sleep(60)

    time.sleep(20)