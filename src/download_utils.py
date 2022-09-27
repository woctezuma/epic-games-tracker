from src.page_mapping_utils import get_sandbox_id
from src.query_page_mapping import to_page_mapping
from src.query_store_data import to_store_data
from src.store_data_utils import get_total_num_store_elements, get_page_slugs

MAX_STEP_SIZE = 1000


def download_page_slugs(include_dlc=False):
    dummy_store_data = to_store_data(cursor=0, step=1, include_dlc=include_dlc)
    num_elements = get_total_num_store_elements(dummy_store_data)

    page_slugs = []

    for cursor in range(0, num_elements, MAX_STEP_SIZE):
        print(f'Cursor = {cursor}')
        store_data = to_store_data(cursor=cursor, step=MAX_STEP_SIZE, include_dlc=include_dlc)
        page_slugs += get_page_slugs(store_data)

    return page_slugs


def download_page_mappings(page_slugs, known_page_mappings=None):
    if known_page_mappings is None:
        known_page_mappings = dict()

    page_mappings = known_page_mappings
    num_slugs = len(page_slugs)

    for i, slug in enumerate(sorted(page_slugs), start=1):
        print(f'[{i}/{num_slugs}] {slug}')

        if slug not in page_mappings:
            mapping_data = to_page_mapping(slug)
            page_mappings[slug] = get_sandbox_id(mapping_data)

    return page_mappings
