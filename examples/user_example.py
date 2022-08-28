import os
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# Load authentication token
load_dotenv()
msToken: str = os.environ.get("msToken")

with TikTokApi(msToken=msToken) as api: 
    user = api.user(username="therock")

    print(user.info_full())

    for video in user.videos():
        print(video.id)

    for liked_video in api.user(username="public_likes").videos():
        print(liked_video.id)
