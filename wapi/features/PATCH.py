from functools import wraps

from requests import Response

from wapi.features.request import make_request
from wapi.static.T import T
from wapi.static.methods import HTTPMethod
from wapi.utils.get_path import get_path


def PATCH(
        path: str = "",
        _T: T = None
) -> T | Response:
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            p = get_path(self, func, path)

            return make_request(
                url=p,
                method=HTTPMethod.PATCH,
                _T=_T,
                data=kwargs
            )

        return wrapper

    return decorator
