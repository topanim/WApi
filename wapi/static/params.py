class WApiParams:
    HEADERS = "headers"
    PARAMS = "params"
    BODY = "body"
    FILES = "files"
    TIMEOUT = "timeout"
    REDIRECT = "redirect"
    COOKIES = "cookies"

    @classmethod
    def get_params(cls):
        return [
            cls.HEADERS,
            cls.PARAMS,
            cls.BODY,
            cls.FILES,
            cls.TIMEOUT,
            cls.REDIRECT,
            cls.COOKIES
        ]


class RequestParams:
    URL = "url"
    HEADERS = "headers"
    PARAMS = "params"
    BODY = "data"
    FILES = "files"
    TIMEOUT = "timeout"
    REDIRECT = "allow_redirects"
    COOKIES = "cookies"

    @classmethod
    def get_params(cls):
        return [
            cls.HEADERS,
            cls.PARAMS,
            cls.BODY,
            cls.FILES,
            cls.TIMEOUT,
            cls.REDIRECT,
            cls.COOKIES
        ]
