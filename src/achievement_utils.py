def list_all_unlock_percentages(achievement_data):
    return [e['achievement']['rarity']['percent'] for e in achievement_data['achievements']]


def compute_max_unlock_percentage(achievement_data):
    rarity_list = list_all_unlock_percentages(achievement_data)

    if len(rarity_list) > 0:
        rarity = max(rarity_list)
    else:
        rarity = None

    return rarity


def list_base_achievement_sets(achievement_data):
    return [e for e in achievement_data["achievementSets"] if e['isBase']]


def get_main_achievement_set(achievement_data):
    base_achievement_sets = list_base_achievement_sets(achievement_data)
    return base_achievement_sets[0]


def summarize_achievement(achievement_data):
    achievement_summary = get_main_achievement_set(achievement_data)
    achievement_summary['maxRarity'] = compute_max_unlock_percentage(achievement_data)

    return achievement_summary
