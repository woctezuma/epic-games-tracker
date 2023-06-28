def list_all_unlock_percentages(achievement_data):
    return [e['achievement']['rarity']['percent'] for e in achievement_data['achievements']]


def compute_max_unlock_percentage(achievement_data):
    rarity_list = list_all_unlock_percentages(achievement_data)

    if len(rarity_list) > 0:
        rarity = max(rarity_list)
    else:
        rarity = None

    return rarity


def list_all_achievement_sets(achievement_data):
    return achievement_data["achievementSets"]


def list_base_achievement_sets(achievement_data):
    return [e for e in list_all_achievement_sets(achievement_data) if e['isBase']]


def sort_achievement_sets_by_num_players(achievement_sets):
    return sorted(achievement_sets, key=lambda x: int(x['numProgressed']), reverse=True)


def get_main_achievement_set(achievement_data):
    base_achievement_sets = list_base_achievement_sets(achievement_data)
    if len(base_achievement_sets) == 0:
        base_achievement_sets = list_all_achievement_sets(achievement_data)
    if len(base_achievement_sets) > 1:
        base_achievement_sets = sort_achievement_sets_by_num_players(base_achievement_sets)
    return base_achievement_sets[0]


def summarize_achievement(achievement_data):
    achievement_summary = get_main_achievement_set(achievement_data)
    achievement_summary['maxRarity'] = compute_max_unlock_percentage(achievement_data)

    return achievement_summary


def create_dummy_dictionary(field):
    return {s: None for s in field}
