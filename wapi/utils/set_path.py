from wapi.utils.merge_paths import merge_paths


def set_path(obj):
    for name, cls in vars(obj).items():
        if hasattr(cls, 'path'):
            cls.__class__.path = merge_paths(obj.path, cls.path)
            set_path(cls.__class__)
