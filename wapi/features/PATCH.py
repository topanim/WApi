import inspect
from functools import wraps

from requests import Response

from wapi.features.request import make_request, async_make_request
from wapi.static.T import T
from wapi.static.methods import HTTPMethod
from wapi.utils.get_path import get_path


def PATCH(
        path: str = "",
        _T: T = None
) -> T | Response:
    def decorator(func):
        @wraps(func)
        def sync_wrapper(self, *args, **kwargs):
            p = get_path(self, func, path)

            return make_request(
                url=p,
                method=HTTPMethod.GET,
                _T=_T,
                data=kwargs
            )

        @wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            p = get_path(self, func, path)

            return await async_make_request(
                url=p,
                method=HTTPMethod.GET,
                _T=_T,
                data=kwargs
            )

        is_coroutine = inspect.iscoroutinefunction(func)
        if is_coroutine:
            return async_wrapper
        else:
            return sync_wrapper

    return decorator
