def list_all_unlock_percentages(achievement_data):
    return [e['achievement']['rarity']['percent'] for e in achievement_data['achievements']]


def compute_max_unlock_percentage(achievement_data):
    rarity_list = list_all_unlock_percentages(achievement_data)

    if len(rarity_list) > 0:
        rarity = max(rarity_list)
    else:
        rarity = None

    return rarity


def get_main_achievement_set(achievement_data):
    return achievement_data["achievementSets"][0]


def summarize_achievement(achievement_data):
    achievement_summary = get_main_achievement_set(achievement_data)
    achievement_summary['maxRarity'] = compute_max_unlock_percentage(achievement_data)

    return achievement_summary
