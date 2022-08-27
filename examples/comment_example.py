import os
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# Load authentication token
load_dotenv()
msToken: str = os.environ.get("msToken")

with TikTokApi(msToken=msToken) as api:
    tiktok_video_id = 7107272719166901550
    video = api.video(id=tiktok_video_id)

    for comment in video.comments():
        print(comment.text)
