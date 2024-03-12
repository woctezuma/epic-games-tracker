import operator

DUMMY_SUFFIX = '/home'
DUMMY_PAGE_SLUG_SUFFIXES = ["-bundle", "--premium-edition"]


def get_offer_slug(store_element):
    offers = store_element["offerMappings"]
    if offers is not None and len(offers) > 0:
        offer_slug = offers[0]["pageSlug"]
    else:
        offer_slug = None

    return offer_slug


def is_a_dummy_mapping(mapping):
    return any(mapping["pageSlug"].endswith(s) for s in DUMMY_PAGE_SLUG_SUFFIXES)


def filter_out_dummy_mappings(mappings):
    return [e for e in mappings if not is_a_dummy_mapping(e)]


def get_namespace_slug(store_element):
    namespace_catalog = store_element.get("catalogNs")
    mappings = None if namespace_catalog is None else namespace_catalog.get('mappings')
    if mappings is not None and len(mappings) > 0:
        if len(mappings) > 1:
            mappings = filter_out_dummy_mappings(mappings)
        namespace_slug = mappings[0]["pageSlug"]
    else:
        namespace_slug = None

    return namespace_slug


def get_product_slug(store_element):
    product_slug = store_element["productSlug"]
    if product_slug is not None:
        product_slug = product_slug.removesuffix(DUMMY_SUFFIX)
    return product_slug


get_url_slug = operator.itemgetter('urlSlug')


def to_slug(store_element):
    offer_slug = get_offer_slug(store_element)
    namespace_slug = get_namespace_slug(store_element)
    product_slug = get_product_slug(store_element)
    url_slug = get_url_slug(store_element)

    if offer_slug is not None:
        slug = offer_slug
    elif namespace_slug is not None:
        slug = namespace_slug
    elif product_slug is not None:
        slug = product_slug
    else:
        slug = url_slug

    return slug
