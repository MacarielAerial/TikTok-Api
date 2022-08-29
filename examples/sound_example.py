import os
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# Load authentication token
load_dotenv()
msToken: str = os.environ.get("msToken")

with TikTokApi(msToken=msToken) as api:
    sound = api.sound(id="7134088844828183302")
    print(sound.info_full(use_html=True))

    for video in sound.videos():
        print(video.id)
