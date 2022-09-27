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
