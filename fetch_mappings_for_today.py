from pathlib import Path

from src.data_utils import PAGE_SLUGS_FNAME, PAGE_MAPPINGS_FNAME, SANDBOX_IDS_FNAME
from src.data_utils import load_tracked_page_mappings, load_all_page_mappings
from src.discord_utils import post_slugs_to_discord
from src.download_utils import download_achievement_support_to_filter_page_mappings
from src.download_utils import download_page_slugs, download_page_mappings
from src.json_utils import save_json, load_json
from src.page_mapping_utils import filter_page_mappings_based_on_slugs
from src.utils import sort_dict_by_key, extract_list_difference
from src.webhook_utils import WEBHOOK_KEYWORD_NEW, WEBHOOK_KEYWORD_TROPHY


def main():
    force_update = True

    if force_update or not Path(PAGE_SLUGS_FNAME).exists():
        print('Updating page slugs.')
        page_slugs = download_page_slugs(include_dlc=False)
        save_json(sorted(page_slugs), PAGE_SLUGS_FNAME, prettify=True)
    else:
        page_slugs = load_json(PAGE_SLUGS_FNAME)

    print('Updating all page mappings.')
    known_page_mappings = load_all_page_mappings()
    page_mappings = download_page_mappings(page_slugs, known_page_mappings=known_page_mappings)
    save_json(sort_dict_by_key(page_mappings), PAGE_MAPPINGS_FNAME, prettify=True)

    new_game_slugs = extract_list_difference(page_mappings, known_page_mappings)
    post_slugs_to_discord(new_game_slugs, webhook_keyword=WEBHOOK_KEYWORD_NEW)

    print('Updating tracked page mappings.')
    page_mappings_of_interest = filter_page_mappings_based_on_slugs(page_mappings, page_slugs)
    known_support = load_tracked_page_mappings()
    sandbox_ids_dict = download_achievement_support_to_filter_page_mappings(page_mappings_of_interest,
                                                                            known_support=known_support)
    save_json(sort_dict_by_key(sandbox_ids_dict), SANDBOX_IDS_FNAME, prettify=True)

    new_tracked_game_slugs = extract_list_difference(sandbox_ids_dict, known_support)
    post_slugs_to_discord(new_tracked_game_slugs, webhook_keyword=WEBHOOK_KEYWORD_TROPHY)

    return


if __name__ == '__main__':
    main()
