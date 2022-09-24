import time

from src.achievement_utils import summarize_achievement
from src.fields import RAW_RATING_FIELDS, ACHIEVEMENT_FIELDS
from src.query_achievement import to_achievement
from src.query_game_rating import to_game_rating

COOLDOWN_DURATION_IN_SECONDS = 2


def fetch_data_for_single_id(sandbox_id):
    data = dict()

    game_rating = to_game_rating(sandbox_id)

    if game_rating is None:
        print(f'Try again {sandbox_id} in {COOLDOWN_DURATION_IN_SECONDS}s.')
        time.sleep(COOLDOWN_DURATION_IN_SECONDS)
        game_rating = to_game_rating(sandbox_id)

    for s in RAW_RATING_FIELDS:
        try:
            data[s] = game_rating[s]
        except TypeError:
            data[s] = None

    achievement = to_achievement(sandbox_id)
    achievement_summary = summarize_achievement(achievement)

    for s in ACHIEVEMENT_FIELDS:
        data[s] = achievement_summary[s]

    return data


def fetch_data_for_several_ids(sandbox_ids, verbose=True):
    data = {}
    num_sandbox_ids = len(sandbox_ids)

    for i, sandbox_id in enumerate(sandbox_ids, start=1):
        if verbose:
            print(f"[{i:3}/{num_sandbox_ids}] {sandbox_id}")
        data[sandbox_id] = fetch_data_for_single_id(sandbox_id)

    return data
