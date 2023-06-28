from src.achievement_utils import summarize_achievement
from src.fields import RAW_RATING_FIELDS, ACHIEVEMENT_FIELDS
from src.query_game_data import to_game_data
from src.retry_utils import is_buggy_achievement_data
from src.utils import create_dummy_dictionary


def fetch_data_for_single_id(sandbox_id):
    data = dict()

    achievement, game_rating = to_game_data(sandbox_id)

    if achievement is None or is_buggy_achievement_data(achievement):
        print(f'[ERROR] achievement data cannot be found for {sandbox_id}.')
        achievement_summary = create_dummy_dictionary(ACHIEVEMENT_FIELDS)
    else:
        achievement_summary = summarize_achievement(achievement)

    for s in ACHIEVEMENT_FIELDS:
        data[s] = achievement_summary[s]

    if game_rating is None:
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
        data[sandbox_id] = fetch_data_for_single_id(sandbox_id)

    return data
