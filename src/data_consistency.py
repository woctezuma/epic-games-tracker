def has_consistent_average_rating(v):
    return v['averageRating'] is not None and 1 <= v['averageRating'] <= 5


def has_consistent_rating_count(v):
    return v['ratingCount'] is not None and v['ratingCount'] >= 0


def has_consistent_num_players(v):
    return v['numProgressed'] is not None and v['numProgressed'] >= 0


def has_consistent_num_platinum(v):
    values_are_numerical = v['numProgressed'] is not None and v['numCompleted'] is not None
    return values_are_numerical and 0 <= v["numCompleted"] <= v['numProgressed']


def has_consistent_max_rarity(v):
    return v['maxRarity'] is not None and 0 <= v['maxRarity'] <= 100


def has_consistent_stats(v):
    has_consistent_ratings = has_consistent_average_rating(v) and has_consistent_rating_count(v)
    has_consistent_players = has_consistent_num_players(v) and has_consistent_num_platinum(v)
    has_consistent_achievements = has_consistent_max_rarity(v)
    return has_consistent_ratings and has_consistent_players and has_consistent_achievements
