from functools import wraps
from typing import Type

from wapi.utils.is_class import is_class


def Route(path: str):
    def decorator(obj: Type[object]):
        def class_wrapper():

            if obj.__name__ == 'SawakoAPI':
                print(obj.__class__)
                print(vars(obj.__class__))
                print(vars(obj))

            if hasattr(obj, 'path'):
                obj.path += path
            else:
                obj.path = path

            if obj.__name__ == 'SawakoAPI':
                #     print(path)
                #     print(obj)
                #     print(obj.path)
                print('-----cicle----------')

            for name, cls in vars(obj).items():
                if obj.__name__ == 'SawakoAPI':
                    print(cls.__class__)

                if hasattr(cls, 'path'):
                    if obj.__name__ == 'SawakoAPI':
                        print(f"has path {cls.path}")
                        print(cls)
                        print(cls.__class__)
                    cls.__class__.path = obj.path + cls.path
                    if obj.__name__ == 'SawakoAPI':
                        print(f"new path is {cls.path}")
                        print(f"new class path is {cls.__class__.path}")

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
