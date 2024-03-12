def get_num_achievements(achievement_data):
    try:
        num_achievements = achievement_data["totalAchievements"]
    except (TypeError, KeyError):
        num_achievements = None
    return num_achievements


def supports_achievements(achievement_data):
    num_achievements = get_num_achievements(achievement_data)
    return bool(num_achievements is not None)
