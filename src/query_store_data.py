from src.api import send_post_request_to_api


def get_params_to_query_store_data(cursor, step, include_dlc=False):
    if include_dlc:
        category_str = ""
    else:
        category_str = 'category: "games/edition/base", '

    query_str = "{Catalog {searchStore"
    query_str += f'({category_str}start: {cursor}, count: {step}) '
    query_str += "{"
    query_str += "paging {total} elements {offerMappings {pageSlug}}"
    query_str += "}}}"

    params = {"query": query_str}

    return params


def to_store_data(cursor, step, include_dlc=False, verbose=True):
    params = get_params_to_query_store_data(cursor, step, include_dlc)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        store_data = data["data"]["Catalog"]["searchStore"]
    except (TypeError, KeyError) as e:
        store_data = None
    return store_data
