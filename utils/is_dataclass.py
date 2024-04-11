from typing import Type


def is_dataclass(cls: Type[object]) -> bool:
    return hasattr(cls, "__dataclass_fields__")
