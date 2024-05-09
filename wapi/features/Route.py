from functools import wraps
from typing import Type

from wapi.utils.is_class import is_class
from wapi.utils.set_path import set_path


def Route(path: str):
    def decorator(obj: Type[object]):
        def class_wrapper():
            if hasattr(obj, 'path'):
                obj.path += path
            else:
                obj.path = path

            set_path(obj)

            return obj

        @wraps(obj)
        def func_wrapper(self, *args, **kwargs):
            if hasattr(obj.__wrapped__, 'path'):
                obj.__wrapped__.path = path + obj.__wrapped__.path
            else:
                obj.__wrapped__.path = path

            return obj(self, *args, **kwargs)

        if is_class(obj):
            return class_wrapper()
        return func_wrapper

    return decorator
