from src.data_utils import populate_slugs


def has_broken_achievements(data, sandbox_id):
    return data.get(sandbox_id).get('maxRarity') is None


def list_sandbox_ids_with_fixed_achievements(data_yesterday, data_today):
    sandbox_ids = [
        sandbox_id
        for sandbox_id in set(data_yesterday).intersection(data_today)
        if has_broken_achievements(data_yesterday, sandbox_id)
        and not has_broken_achievements(data_today, sandbox_id)
    ]

    return sandbox_ids


def list_slugs_with_fixed_achievements(data_yesterday, data_today):
    sandbox_ids = list_sandbox_ids_with_fixed_achievements(data_yesterday, data_today)
    data_today = populate_slugs(data_today)
    game_slugs = [data_today[sandbox_id]['slug'] for sandbox_id in sandbox_ids]
    return game_slugs
