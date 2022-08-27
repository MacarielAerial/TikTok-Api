import os
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# Load authentication token
load_dotenv()
msToken: str = os.environ.get("msToken")

with TikTokApi(msToken=msToken) as api:
    tag = api.hashtag(name="funny")

    print(tag.info())

    for video in tag.videos():
        print(video.id)
