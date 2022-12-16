import operator

get_sandbox_id = operator.itemgetter('sandboxId')


def get_updated_date(mapping_data):
    return mapping_data["updatedDate"]


def filter_page_mappings_based_on_slugs(page_mappings, page_slugs):
    return {k: v for k, v in page_mappings.items() if k in page_slugs}
