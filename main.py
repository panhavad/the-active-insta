import schedule
import time
from modules import insta_core

def active_like():
    latest_feeds_media_ids = insta_core.get_latest_feeds_media_ids()[0]
    current_like_status = insta_core.like_list_of_media(latest_feeds_media_ids)
    print(latest_feeds_media_ids, current_like_status)

schedule.every(5).seconds.do(active_like)

while 1:
    schedule.run_pending()
    time.sleep(1)
