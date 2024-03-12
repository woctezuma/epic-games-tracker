from src.api import send_post_request_to_api
from src.query_utils import get_query_str_for_ratings


def get_params_to_query_game_rating(sandbox_id):
    query_str = "{"
    query_str += get_query_str_for_ratings(sandbox_id)
    query_str += "}"

    params = {"query": query_str}

    return params


def to_game_rating(sandbox_id, verbose=True):
    params = get_params_to_query_game_rating(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        game_rating = data["data"]["RatingsPolls"]["getProductResult"]
    except (TypeError, KeyError):
        game_rating = None
    return game_rating
