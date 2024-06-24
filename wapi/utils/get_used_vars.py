def get_used_vars(path: str, params: dict) -> list[str]:
    keys_in_string = [key.strip('{}') for part in path.split('{') for key in part.split('}') if key]
    used_keys = [key for key in keys_in_string if key in params]

    return used_keys
