import os
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# Load authentication token
load_dotenv()
msToken: str = os.environ.get("msToken")

with TikTokApi(msToken=msToken) as api:
    sound = api.sound(id="7016547803243022337")

    for video in sound.videos():
        print(video.id)
