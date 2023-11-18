from src.data_utils import (
    PAGE_MAPPINGS_FNAME,
    SANDBOX_IDS_FNAME,
    load_all_page_mappings,
    load_tracked_page_mappings,
)
from src.download_utils import (
    download_achievement_support_to_filter_page_mappings,
    download_page_mappings,
)
from src.json_utils import save_json
from src.page_mapping_utils import filter_page_mappings_based_on_slugs
from src.utils import extract_list_difference, sort_dict_by_key


def update_all_page_mappings(page_slugs, known_page_mappings=None):
    if known_page_mappings is None:
        known_page_mappings = load_all_page_mappings()

    page_mappings = download_page_mappings(page_slugs, known_page_mappings=known_page_mappings)
    save_json(sort_dict_by_key(page_mappings), PAGE_MAPPINGS_FNAME, prettify=True)

    new_game_slugs = extract_list_difference(page_mappings, known_page_mappings)

    return new_game_slugs


def update_tracked_page_mappings(page_slugs, known_page_mappings=None):
    if known_page_mappings is None:
        known_page_mappings = load_all_page_mappings()

    page_mappings_of_interest = filter_page_mappings_based_on_slugs(known_page_mappings, page_slugs)

    known_support = load_tracked_page_mappings()
    sandbox_ids_dict = download_achievement_support_to_filter_page_mappings(page_mappings_of_interest,
                                                                            known_support=known_support)
    save_json(sort_dict_by_key(sandbox_ids_dict), SANDBOX_IDS_FNAME, prettify=True)

    new_tracked_game_slugs = extract_list_difference(sandbox_ids_dict, known_support)

    return new_tracked_game_slugs
