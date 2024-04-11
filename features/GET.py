from functools import wraps

from jsons import load
from requests import Response, get

from static.T import T
from utils.get_path import get_path


def GET(
        path: str = "",
        _T: T = None,
        *,
        auto: bool = False,
        unpack: bool = False
) -> T | Response:
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            headers = kwargs.pop("headers")
            p = get_path(self, func, path)

            if auto:
                if unpack and (body := kwargs.pop('body')):
                    kwargs.update(body)

                url = p + "?" + "&".join([f'{k}={v}' for k, v in kwargs.items()])
            else:
                url = p.format(*args, **kwargs)

            response = get(url, headers=headers)

            if _T is None:
                return response
            return load(response.json(), _T)

        return wrapper

    return decorator
