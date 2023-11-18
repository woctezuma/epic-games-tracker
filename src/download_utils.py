import copy

from src.achievement_support_utils import supports_achievements
from src.page_mapping_utils import get_sandbox_id
from src.query_achievement_support import to_achievement_support
from src.query_page_mapping import to_page_mapping
from src.query_store_data import to_store_data
from src.store_data_utils import get_page_slugs, get_total_num_store_elements

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

    page_mappings = copy.deepcopy(known_page_mappings)
    num_slugs = len(page_slugs)

    for i, slug in enumerate(sorted(page_slugs), start=1):
        print(f'[{i}/{num_slugs}] {slug}')

        if slug not in page_mappings:
            mapping_data = to_page_mapping(slug)
            if mapping_data is not None:
                page_mappings[slug] = get_sandbox_id(mapping_data)

    return page_mappings


def download_achievement_support_to_filter_page_mappings(page_mappings, known_support=None):
    if known_support is None:
        known_support = dict()

    support = copy.deepcopy(known_support)
    num_slugs = len(page_mappings)

    achievement_support_dict = dict()

    for i, slug in enumerate(sorted(page_mappings, key=lambda x: (len(x), x)), start=1):
        print(f'[{i}/{num_slugs}] {slug}')

        if slug not in support:
            sandbox_id = page_mappings[slug]

            if sandbox_id not in achievement_support_dict:
                achievement_support_dict[sandbox_id] = to_achievement_support(sandbox_id)

            achievement_data = achievement_support_dict[sandbox_id]

            if supports_achievements(achievement_data):
                support[slug] = sandbox_id

    return support
