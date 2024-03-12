import operator

from src.slug_utils import to_slug


def get_total_num_store_elements(store_data):
    return store_data["paging"]["total"]


get_store_elements = operator.itemgetter('elements')


def get_page_slug(store_element):
    try:
        page_slug = to_slug(store_element)
    except (IndexError, KeyError, TypeError):
        page_slug = None

    return page_slug


def is_a_relevant_page_slug(page_slug):
    return bool(page_slug is not None and len(page_slug) > 0)


def get_page_slugs(store_data):
    slugs = [get_page_slug(e) for e in get_store_elements(store_data)]
    return [s for s in slugs if is_a_relevant_page_slug(s)]
