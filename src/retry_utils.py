def is_buggy_game_rating_data(game_rating):
    return game_rating is None

def has_buggy_achievement_sets(achievement):
    return len(achievement['achievementSets']) == 0


def has_buggy_achievements(achievement):
    return achievement['achievements'] is None


def is_buggy_achievement_data(achievement):
    return has_buggy_achievement_sets(achievement) or has_buggy_achievements(achievement)


