from typing import Callable


def get_path(cls: type, f: Callable, path: str):
    abs_path = ""

    if hasattr(cls.__class__, 'path'):
        abs_path += getattr(cls.__class__, 'path') + abs_path

    if hasattr(f, 'path'):
        abs_path += getattr(f, 'path')

    return abs_path + path
