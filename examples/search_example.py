import os
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# Load authentication token
load_dotenv()
msToken: str = os.environ.get("msToken")

with TikTokApi(msToken=msToken) as api:
    for user in api.search.users("therock"):
        print(user.username)

    for video in api.search.videos("funny"):
        print(video.id)
