from functools import wraps
from typing import Type

from wapi.utils.is_class import is_class


def Route(path: str):
    def decorator(obj: Type[object]):
        def class_wrapper():
            if hasattr(obj.__class__, 'path'):
                obj.path += path
            else:
                obj.path = path

            for name, cls in vars(obj).items():
                if hasattr(cls.__class__, 'path'):
                    cls.__class__.path = obj.path + cls.path

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