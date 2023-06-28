import backoff
import requests

GRAPHQL_API_URL = "https://graphql.epicgames.com/graphql"


def send_post_request_to_api(json_data, verbose=True):
    r = to_response(json_data)
    return to_data(r, verbose=verbose)


@backoff.on_predicate(backoff.expo, lambda r: not r.ok, max_tries=3)
def to_response(json_data):
    return requests.post(GRAPHQL_API_URL, json=json_data)


def to_data(response, verbose=True):
    if response.ok:
        data = response.json()
    else:
        data = None
        if verbose:
            print(f"Status code = {response.status_code}")
    return data
