def has_at_lease_one_none_element(v):
    return any(e is None for e in v.values())


def hide_games_with_none_elements(data):
    return {k: v for k, v in data.items() if not has_at_lease_one_none_element(v)}


def has_players(v):
    return bool(v['numProgressed'] is not None and v['numProgressed'] > 0)


def hide_games_with_zero_player(data):
    return {k: v for k, v in data.items() if has_players(v)}


def has_at_least_one_unlocked_achievement(v):
    return bool(v['maxRarity'] is not None and v['maxRarity'] > 0)


def has_working_achievements(v):
    return has_at_least_one_unlocked_achievement(v) and v['maxRarity'] <= 100


def hide_games_with_buggy_achievements(data):
    return {k: v for k, v in data.items() if has_working_achievements(v)}
