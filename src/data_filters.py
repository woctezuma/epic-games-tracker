from src.data_consistency import has_consistent_stats


def hide_games_with_inconsistent_stats(data):
    return {k: v for k, v in data.items() if has_consistent_stats(v)}


def has_all_stats_filled_in(v):
    return all(e is not None for e in v.values())


def hide_games_missing_a_stat(data):
    return {k: v for k, v in data.items() if has_all_stats_filled_in(v)}


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
