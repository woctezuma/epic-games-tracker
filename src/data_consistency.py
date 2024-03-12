MIN_NUM_STARS = 1
MAX_NUM_STARS = 5
MAX_PERCENTAGE = 100

def has_consistent_average_rating(v):
    return v['averageRating'] is not None and MIN_NUM_STARS <= v['averageRating'] <= MAX_NUM_STARS


def has_consistent_rating_count(v):
    return v['ratingCount'] is not None and v['ratingCount'] >= 0


def has_consistent_num_players(v):
    return v['numProgressed'] is not None and v['numProgressed'] >= 0


def has_consistent_num_platinum(v):
    values_are_numerical = v['numProgressed'] is not None and v['numCompleted'] is not None
    return values_are_numerical and 0 <= v["numCompleted"] <= v['numProgressed']


def has_consistent_max_rarity(v):
    return v['maxRarity'] is not None and 0 <= v['maxRarity'] <= MAX_PERCENTAGE


def has_consistent_stats(v):
    has_consistent_ratings = has_consistent_average_rating(v) and has_consistent_rating_count(v)
    has_consistent_players = has_consistent_num_players(v) and has_consistent_num_platinum(v)
    has_consistent_achievements = has_consistent_max_rarity(v)
    return (
        has_consistent_ratings
        and has_consistent_players
        and has_consistent_achievements
    )
