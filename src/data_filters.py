def hide_none_elements(data):
    return {k: v for k, v in data.items() if all(e is not None for e in v.values())}
