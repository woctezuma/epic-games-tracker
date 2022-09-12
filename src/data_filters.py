def has_at_lease_one_none_element(v):
    return any(e is None for e in v.values())


def hide_none_elements(data):
    return {k: v for k, v in data.items() if not has_at_lease_one_none_element(v)}
