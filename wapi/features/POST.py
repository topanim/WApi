from functools import wraps

from jsons import load, dump
from requests import Response, post

from wapi.static.T import T
from wapi.utils.get_path import get_path


def POST(
        path: str = "",
        _T: T = None,
) -> T | Response:
    def decorator(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            headers = kwargs.pop('headers', None)
            data = dict()

            if body := dump(kwargs.pop('body', None)):
                data.update(body)

            if not kwargs:
                data.update(kwargs)

            url = get_path(self, func, path)
            response = post(url, json=data, headers=headers)

            if _T is None:
                return response
            return load(response.json(), _T)

        return wrapper

    return decorator
