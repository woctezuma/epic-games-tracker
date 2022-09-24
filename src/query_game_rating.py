from src.api import send_post_request_to_api


def get_params_to_query_game_rating(sandbox_id):
    query_str = "{RatingsPolls {getProductResult"
    query_str += f'(sandboxId: "{sandbox_id}", locale: "en") '
    query_str += "{"
    query_str += "averageRating pollResult {id total}"
    query_str += "}}}"

    params = {"query": query_str}

    return params


def to_game_rating(sandbox_id, verbose=True):
    params = get_params_to_query_game_rating(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        game_rating = data["data"]["RatingsPolls"]["getProductResult"]
    except (TypeError, KeyError) as e:
        game_rating = None
    return game_rating
