from src.achievement_utils import summarize_achievement
from src.fields import ACHIEVEMENT_FIELDS, RAW_RATING_FIELDS
from src.query_game_data import to_game_data
from src.retry_utils import has_no_achievement, has_no_rating
from src.utils import create_dummy_dictionary


def fetch_data_for_single_id(sandbox_id, verbose=True):
    data = {}

    achievement, game_rating = to_game_data(sandbox_id)

    if has_no_achievement(achievement):
        if verbose:
            print(f'[achievement] missing data for {sandbox_id}: {achievement}.')
        achievement_summary = create_dummy_dictionary(ACHIEVEMENT_FIELDS)
    else:
        achievement_summary = summarize_achievement(achievement)

    for s in ACHIEVEMENT_FIELDS:
        data[s] = achievement_summary[s]

    if has_no_rating(game_rating):
        if verbose:
            print(f'[rating] missing data for {sandbox_id}.')
        game_rating = create_dummy_dictionary(RAW_RATING_FIELDS)

    for s in RAW_RATING_FIELDS:
        data[s] = game_rating[s]

    return data


def fetch_data_for_several_ids(sandbox_ids, verbose=True):
    data = {}
    num_sandbox_ids = len(sandbox_ids)

    for i, sandbox_id in enumerate(sandbox_ids, start=1):
        if verbose:
            print(f"[{i:3}/{num_sandbox_ids}] {sandbox_id}")
        data[sandbox_id] = fetch_data_for_single_id(sandbox_id, verbose=verbose)

    return data
