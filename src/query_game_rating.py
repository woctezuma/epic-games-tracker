from src.api import send_post_request_to_api


def get_params_to_query_game_rating(sandbox_id):
    params = {
        "operationName": "getProductResult",
        "variables": {"sandboxId": sandbox_id, "locale": "en"},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "b6795ca724814d54cfc1854698773d1ee7b0721b326f64fc08b48a3b9358b01d",
            }
        },
    }

    return params


def to_game_rating(sandbox_id, verbose=True):
    params = get_params_to_query_game_rating(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        game_rating = data["data"]["RatingsPolls"]["getProductResult"]
    except (TypeError, KeyError) as e:
        game_rating = None
    return game_rating
