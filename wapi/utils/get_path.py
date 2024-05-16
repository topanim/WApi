from typing import Callable


def get_path(cls: type, f: Callable, path: str):
    abs_path = ""

    if hasattr(type(cls), 'path'):
        abs_path += getattr(type(cls), 'path') + abs_path

    if hasattr(f, 'path'):
        abs_path += getattr(f, 'path')

    return abs_path + path
