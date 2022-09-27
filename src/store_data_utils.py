def get_total_num_store_elements(store_data):
    return store_data["paging"]["total"]


def get_store_elements(store_data):
    return store_data["elements"]


def get_page_slug(store_element):
    try:
        page_slug = store_element["offerMappings"]["pageSlug"]
    except KeyError:
        page_slug = None

    return page_slug


def is_a_relevant_page_slug(page_slug):
    return bool(page_slug is not None and len(page_slug) > 0)


def get_page_slugs(store_data):
    slugs = [get_page_slug(e) for e in get_store_elements(store_data)]
    return [s for s in slugs if is_a_relevant_page_slug(s)]
