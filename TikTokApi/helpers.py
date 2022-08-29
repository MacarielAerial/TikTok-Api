import json
from bs4 import BeautifulSoup
from typing import Any, Dict
from TikTokApi.browser_utilities.browser import browser
from urllib.parse import quote, urlencode
from .exceptions import *

import re
import requests


def extract_tag_contents(html: str) -> Dict[str, Any]:
    soup = BeautifulSoup(html)
    json_s = soup.find("script", type="application/json").string
    return json.loads(json_s)


def extract_video_id_from_url(url, headers={}):
    url = requests.head(url=url, allow_redirects=True, headers=headers).url
    if "@" in url and "/video/" in url:
        return url.split("/video/")[1].split("?")[0]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )
