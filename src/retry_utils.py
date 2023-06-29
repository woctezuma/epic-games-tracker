def has_buggy_achievement_sets(achievement):
    return len(achievement['achievementSets']) == 0


def has_buggy_achievements(achievement):
    return achievement['achievements'] is None


def has_no_achievement(achievement):
    return has_buggy_achievement_sets(achievement) or has_buggy_achievements(achievement)


