def get_sandbox_id(mapping_data):
    return mapping_data["sandboxId"]


def filter_page_mappings_based_on_slugs(page_mappings, page_slugs):
    return {k: v for k, v in page_mappings.items() if k in page_slugs}
