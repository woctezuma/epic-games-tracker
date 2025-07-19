import cloudscraper

from src.api import send_post_request_to_api


def get_params_to_query_store_data(cursor, step, include_dlc=False):
    category_str = "" if include_dlc else 'category: "games/edition/base", '

    query_str = "{Catalog {searchStore"
    query_str += f'({category_str}start: {cursor}, count: {step}) '
    query_str += "{"
    query_str += 'paging {total} elements {offerMappings {pageSlug} catalogNs {mappings(pageType: "productHome") {pageSlug}} productSlug urlSlug}'
    query_str += "}}}"

    params = {"query": query_str}

    return params


def to_store_data(cursor, step, scraper: cloudscraper.CloudScraper | None = None, *, include_dlc=False, verbose=True):
    if scraper is None:
        scraper = cloudscraper.create_scraper()

    params = get_params_to_query_store_data(cursor, step, include_dlc)
    data = send_post_request_to_api(params, scraper=scraper, verbose=verbose)
    try:
        store_data = data["data"]["Catalog"]["searchStore"]
    except (TypeError, KeyError):
        store_data = None
    return store_data
