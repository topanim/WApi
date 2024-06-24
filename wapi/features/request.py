from dataclasses import asdict, is_dataclass
from typing import Union

import aiohttp
import requests
from aiohttp import ClientResponse
from jsons import load
from requests import Response

from wapi.static.T import T
from wapi.static.params import WApiParams, RequestParams
from wapi.utils.get_used_vars import get_used_vars


def make_request(
        url: str,
        method: str,
        _T: T = None,
        data: dict = None,
) -> Union[T | Response]:
    files: dict = data.pop(WApiParams.FILES, None)

    response = requests.request(
        method=method,
        **get_common_request_params(data, url),
        files=files
    )

    if _T is None:
        return data
    return load(response.json(), _T)


async def async_make_request(
        url: str,
        method: str,
        _T: T = None,
        data: dict = None,
) -> Union[T | ClientResponse]:
    async with aiohttp.ClientSession() as session:
        async with session.request(
                method=method,
                **get_common_request_params(data, url)
        ) as response:
            if _T is None:
                return data
            return load(await response.json(), _T)


def get_common_request_params(
        data: dict,
        url: str
) -> dict:
    headers: dict = data.pop(WApiParams.HEADERS, None)
    cookies: dict = data.pop(WApiParams.COOKIES, None)
    redirect: bool = data.pop(WApiParams.REDIRECT, True)

    if is_dataclass(params := data.pop(WApiParams.PARAMS, None)):
        params = asdict(params)

    if is_dataclass(body := data.pop(WApiParams.BODY, None)):
        body = asdict(body)

    if params is not None:
        used_params = get_used_vars(url, params)
        url = url.format(**params)

        for used_param in used_params:
            params.pop(used_param)

    return {
        RequestParams.URL: url,
        RequestParams.HEADERS: headers,
        RequestParams.COOKIES: cookies,
        RequestParams.REDIRECT: redirect,
        RequestParams.BODY: body,
        RequestParams.PARAMS: params
    }
