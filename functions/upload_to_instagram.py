import requests

# Reference: https://developers.facebook.com/docs/instagram-api/guides/content-publishing


class Instagram:
    def __init__(self, access_token, client_id, client_secret, instagram_page_id):
        print(access_token, client_id, client_secret, instagram_page_id)
        self.client_id = client_id
        self.client_secret = client_secret
        self.instagram_page_id = instagram_page_id
        self.access_token = access_token
        self.refresh_token()


    def get_long_lived_token(self):
        print(self.client_id, self.client_secret, self.access_token)
        request = requests.get("https://graph.facebook.com/v13.0/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(self.client_id, self.client_secret, self.access_token))

        return request.json()['access_token']

    def refresh_token(self):
        self.access_token = self.get_long_lived_token()

    def single_media_post(self, caption, image_url):
        data = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token,
        }

        request = requests.post(
            f"https://graph.facebook.com/v13.0/{self.instagram_page_id}/media", data=data)

        # Returns IG Container ID
        return request.json()['id']


    def publish_container(self, ig_container_id):
        data = {
            "creation_id": ig_container_id,
            "access_token": self.access_token,
        }

        request = requests.post(
            f"https://graph.facebook.com/v13.0/{self.instagram_page_id}/media_publish", data=data)

        # Returns post ID
        return request.json()['id']
