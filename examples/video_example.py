import os
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# Load authentication token
load_dotenv()
msToken: str = os.environ.get("msToken")

with TikTokApi(msToken=msToken) as api: 
    video = api.video(id="7079467984154234158")

    # Bytes of the TikTok video
    video_data = video.bytes()

    with open("out.mp4", "wb") as out_file:
        out_file.write(video_data)
