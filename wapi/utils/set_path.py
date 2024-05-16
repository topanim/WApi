from wapi.utils.merge_paths import merge_paths


def set_path(obj):
    for name, cls in vars(obj).items():
        if hasattr(cls, 'path'):
            type(cls).path = merge_paths(obj.path, cls.path)
            set_path(type(cls))
