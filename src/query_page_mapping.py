from src.api import send_post_request_to_api


def get_params_to_query_page_mapping(page_slug):
    query_str = "{StorePageMapping {mapping"
    query_str += f'(pageSlug: "{page_slug}") '
    query_str += "{"
    query_str += "sandboxId"
    query_str += "}}}"

    params = {"query": query_str}

    return params


def to_page_mapping(page_slug, verbose=True):
    params = get_params_to_query_page_mapping(page_slug)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        store_data = data["data"]["StorePageMapping"]["mapping"]
    except (TypeError, KeyError) as e:
        store_data = None
    return store_data
