import time

from src.achievement_utils import summarize_achievement
from src.fields import RAW_RATING_FIELDS, ACHIEVEMENT_FIELDS
from src.query_achievement import to_achievement
from src.query_game_data import to_game_data
from src.query_game_rating import to_game_rating
from src.retry_utils import is_buggy_achievement_data, is_buggy_game_rating_data

COOLDOWN_DURATION_IN_SECONDS = 2


def fetch_data_for_single_id(sandbox_id):
    data = dict()

    achievement, game_rating = to_game_data(sandbox_id)

    if is_buggy_achievement_data(achievement):
        print(f'Try again {sandbox_id} in {COOLDOWN_DURATION_IN_SECONDS}s.')
        time.sleep(COOLDOWN_DURATION_IN_SECONDS)
        achievement = to_achievement(sandbox_id)

    achievement_summary = summarize_achievement(achievement)

    for s in ACHIEVEMENT_FIELDS:
        data[s] = achievement_summary[s]

    if is_buggy_game_rating_data(game_rating):
        print(f'Try again {sandbox_id} in {COOLDOWN_DURATION_IN_SECONDS}s.')
        time.sleep(COOLDOWN_DURATION_IN_SECONDS)
        game_rating = to_game_rating(sandbox_id)

    for s in RAW_RATING_FIELDS:
        try:
            data[s] = game_rating[s]
        except (TypeError, KeyError) as e:
            data[s] = None

    return data


def fetch_data_for_several_ids(sandbox_ids, verbose=True):
    data = {}
    num_sandbox_ids = len(sandbox_ids)

    for i, sandbox_id in enumerate(sandbox_ids, start=1):
        if verbose:
            print(f"[{i:3}/{num_sandbox_ids}] {sandbox_id}")
        data[sandbox_id] = fetch_data_for_single_id(sandbox_id)

    return data
