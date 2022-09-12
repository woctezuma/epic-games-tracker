def has_at_lease_one_none_element(v):
    return any(e is None for e in v.values())


def hide_games_with_none_elements(data):
    return {k: v for k, v in data.items() if not has_at_lease_one_none_element(v)}


def has_players(v):
    return bool(v['numProgressed'] is not None and v['numProgressed'] > 0)


def hide_games_with_zero_player(data):
    return {k: v for k, v in data.items() if has_players(v)}
