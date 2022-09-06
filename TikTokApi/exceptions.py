from typing import Dict


class TikTokException(Exception):
    """Generic exception that all other TikTok errors are children of."""

    def __init__(self, error_code, raw_response, message):
        self.error_code = error_code
        self.raw_response = raw_response
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.error_code} -> {self.message}'


class CaptchaException(TikTokException):
    """TikTok is showing captcha"""


class NotFoundException(TikTokException):
    """TikTok indicated that this object does not exist."""


class EmptyResponseException(TikTokException):
    """TikTok sent back an empty response."""


class SoundRemovedException(TikTokException):
    """This TikTok sound has no id from being removed by TikTok."""


class InvalidJSONException(TikTokException):
    """TikTok returned invalid JSON."""


class NotAvailableException(TikTokException):
    """The requested object is not available in this region."""

class HashtagNotExistException(TikTokException):
    """The requested hashtag does not exist."""


DICT_STATUS_CODE_TEXT: Dict[str, str] = {
  "0": "OK",
  "450": "CLIENT_PAGE_ERROR",
  "10000": "VERIFY_CODE",
  "10101": "SERVER_ERROR_NOT_500",
  "10102": "USER_NOT_LOGIN",
  "10111": "NET_ERROR",
  "10113": "SHARK_SLIDE",
  "10114": "SHARK_BLOCK",
  "10119": "LIVE_NEED_LOGIN",
  "10202": "USER_NOT_EXIST",
  "10203": "MUSIC_NOT_EXIST",
  "10204": "VIDEO_NOT_EXIST",
  "10205": "HASHTAG_NOT_EXIST",
  "10208": "EFFECT_NOT_EXIST",
  "10209": "HASHTAG_BLACK_LIST",
  "10210": "LIVE_NOT_EXIST",
  "10211": "HASHTAG_SENSITIVITY_WORD",
  "10212": "HASHTAG_UNSHELVE",
  "10213": "VIDEO_LOW_AGE_M",
  "10214": "VIDEO_LOW_AGE_T",
  "10215": "VIDEO_ABNORMAL",
  "10216": "VIDEO_PRIVATE_BY_USER",
  "10217": "VIDEO_FIRST_REVIEW_UNSHELVE",
  "10218": "MUSIC_UNSHELVE",
  "10219": "MUSIC_NO_COPYRIGHT",
  "10220": "VIDEO_UNSHELVE_BY_MUSIC",
  "10221": "USER_BAN",
  "10222": "USER_PRIVATE",
  "10223": "USER_FTC",
  "10224": "GAME_NOT_EXIST",
  "10225": "USER_UNIQUE_SENSITIVITY",
  "10227": "VIDEO_NEED_RECHECK",
  "10228": "VIDEO_RISK",
  "10229": "VIDEO_R_MASK",
  "10230": "VIDEO_RISK_MASK",
  "10231": "VIDEO_GEOFENCE_BLOCK",
  "10404": "FYP_VIDEO_LIST_LIMIT",
  "undefined": "MEDIA_ERROR"
}
