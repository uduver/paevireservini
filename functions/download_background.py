import random
import urllib.request
from datetime import date, datetime
from bs4 import BeautifulSoup

import requests

def download_image(output_path: str) -> bool:
    """Downloads the image from the url and saves it to the file_name.

    Args:
        url (str): The URL to the image.
        output_path (str): The path to save the image to.

    Returns:
        bool: True if the image was downloaded successfully, False otherwise.
    """
    try:
        url: str = get_random_image_url(date.today())
        return urllib.request.urlretrieve(url, output_path)
    except:
        print("The image could not be downloaded.")
        raise

def get_random_image_url(date: date) -> str:
    """Gets a random image URL from pildid.mil.ee.

    Returns:
        str: The URL to the image.
    """
    return random.choice(get_image_urls(date))

def get_image_urls(date: date) -> list:
    """Get latest image urls from pildid.mil.ee.

    Returns:
        list: A list of all of the images
    """

    search_response = requests.post(
        "https://pildid.mil.ee/search.php", data=create_data_for_search_request(date))

    search_soup: BeautifulSoup = BeautifulSoup(
        search_response.text, 'html.parser')
    link_to_last_page: str = str(search_soup.find_all(
        "a", {"class": "page-link"})[-1]).split("\"")[3]

    print("https://pildid.mil.ee/" + link_to_last_page)

    image_count = int(link_to_last_page.split("/")[-1].split("#")[0][6:])
    
    # Get the images from page before the.
    images_page = requests.get(
        "https://pildid.mil.ee/" + link_to_last_page.replace(str(image_count), str(image_count-12)))
    images_soup = BeautifulSoup(images_page.text, 'html.parser')

    thumbnails = images_soup.find("div", {"id": "thumbnails"})
    thumbnail_urls = thumbnails.find_all("img", {"class": "card-img-top"})

    image_urls = []
    for image_url in thumbnail_urls:
        image_name = image_url['src'].split("upload")[1].split("-cu_")[0]
        image_urls.append(f"https://pildid.mil.ee/upload/{image_name}.jpg")

    return image_urls

def create_data_for_search_request(date: date) -> dict:
    """Returns data needed for the post request.

    Args:
        date (date): Todays date.

    Returns:
        dict: Data for the post request that is sent to pildid.mil.ee search endpoint. The start date is 3 days prior to the given date.
    """

    data: dict = {
        'search_allwords': '',
        'mode': 'AND',
        'fields[]': [
            'name',
                'comment',
                'file',
        ],
        'tag_mode': 'AND',
        'date_type': 'date_available',
        'end_day': '0',
        'end_month': '0',
        'end_year': '',
        'subcats-included': '1',
        'submit': 'Submit',
    }

    # Remove 3-days off the current date.
    desired_unix_time: float = datetime.timestamp(
        datetime.combine(date, datetime.min.time())) - 3*86400
    desired_date: date = datetime.fromtimestamp(desired_unix_time).date()

    data['start_day'] = str(desired_date.day)
    data['start_month'] = str(desired_date.month)
    data['start_year'] = str(desired_date.year)
    return data
