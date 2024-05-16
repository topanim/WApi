from dataclasses import asdict, is_dataclass

from jsons import load
from requests import request

from wapi.static.T import T
from wapi.static.params import RequestParams
from wapi.utils.get_used_vars import get_used_vars


def make_request(
        url: str,
        method: str,
        _T: T = None,
        data: dict = None,
):
    headers: dict = data.pop(RequestParams.HEADERS, None)
    params: dict = data.pop(RequestParams.PARAMS, None)
    files: dict = data.pop(RequestParams.FILES, None)
    cookies: dict = data.pop(RequestParams.COOKIES, None)
    redirect: bool = data.pop(RequestParams.REDIRECT, True)
    if is_dataclass(
            body := data.pop(RequestParams.BODY, None)
    ):
        body = asdict(body)

    if params is not None:
        used_params = get_used_vars(url, params)
        url = url.format(**params)

        for used_param in used_params:
            params.pop(used_param)

    response = request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        json=body,
        files=files,
        cookies=cookies,
        allow_redirects=redirect
    )

    if _T is None:
        return response
    return load(response.json(), _T)