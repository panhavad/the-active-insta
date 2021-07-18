import time
import os
from dotenv import load_dotenv
from libs.instagram_private_api import Client, ClientCompatPatch

load_dotenv()

USER_NAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")

api = Client(USER_NAME, PASSWORD)

def get_latest_feeds_media_ids():
    media_ids = []
    media_link = []
    results = api.feed_timeline()
    items = [item for item in results.get('feed_items', [])
            if item.get('media_or_ad')]
    for item in items:
        ClientCompatPatch.media(item['media_or_ad'])
        liked = item['media_or_ad']['has_liked']
        if not liked:
            media_ids.append(item['media_or_ad']['id'])
            media_link.append(item['media_or_ad']['link'])
    return media_ids, media_link

def like_list_of_media(media_ids):
    for media_id in media_ids:
        try:
            res = api.post_like(str(media_id))
            time.sleep(1)
            return res
        except Exception as err:
            return (False, err)
