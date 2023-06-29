from src.api import send_post_request_to_api
from src.query_utils import get_query_str_for_achievements, get_query_str_for_ratings


def get_params_to_query_game_data(sandbox_id):
    query_str = "{"
    query_str += get_query_str_for_achievements(sandbox_id)
    query_str += get_query_str_for_ratings(sandbox_id)
    query_str += "}"

    params = {"query": query_str}

    return params


def to_game_data(sandbox_id, verbose=True):
    params = get_params_to_query_game_data(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)

    try:
        achievement = data["data"]["Achievement"]["productAchievementsRecordBySandbox"]
    except (TypeError, KeyError) as e:
        achievement = None

    try:
        game_rating = data["data"]["RatingsPolls"]["getProductResult"]
    except (TypeError, KeyError) as e:
        game_rating = None

    return achievement, game_rating


def could_arise_from_faulty_request(output):
    return output is None
