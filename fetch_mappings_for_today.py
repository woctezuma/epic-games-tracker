import logging
from pathlib import Path

from src.data_utils import PAGE_SLUGS_FNAME
from src.discord_utils import post_slugs_to_discord
from src.download_utils import download_page_slugs
from src.json_utils import load_json, save_json
from src.time_utils import get_fname_for_today
from src.webhook_utils import (
    WEBHOOK_KEYWORD_LATE_TROPHY,
    WEBHOOK_KEYWORD_NEW,
    WEBHOOK_KEYWORD_TROPHY,
)
from src.workflow_utils import update_all_page_mappings, update_tracked_page_mappings


def main() -> None:
    logging.getLogger('backoff').addHandler(logging.StreamHandler())

    daily_data_fname = get_fname_for_today()
    daily_data_has_already_been_fetched = Path(daily_data_fname).exists()

    if not daily_data_has_already_been_fetched:
        force_update = True

        if force_update or not Path(PAGE_SLUGS_FNAME).exists():
            print('Updating page slugs.')
            page_slugs = download_page_slugs(include_dlc=False)
            save_json(sorted(page_slugs), PAGE_SLUGS_FNAME, prettify=True)
        else:
            page_slugs = load_json(PAGE_SLUGS_FNAME)

        print('Updating all page mappings.')
        new_game_slugs = update_all_page_mappings(page_slugs)
        post_slugs_to_discord(new_game_slugs, webhook_keyword=WEBHOOK_KEYWORD_NEW, turn_into_hyperlinks=True)

        print('Updating tracked page mappings.')
        # First, for new game slugs in order to quickly post to Discord. This should find new tracked slugs in a short time.
        new_tracked_game_slugs = update_tracked_page_mappings(new_game_slugs)
        post_slugs_to_discord(
            new_tracked_game_slugs,
            webhook_keyword=WEBHOOK_KEYWORD_TROPHY,
        )
        # Second, for all the page slugs. This is less rewarding: there are many checks... and very few new tracked slugs!
        new_tracked_game_slugs = update_tracked_page_mappings(page_slugs)
        post_slugs_to_discord(
            new_tracked_game_slugs,
            webhook_keyword=WEBHOOK_KEYWORD_LATE_TROPHY,
        )


if __name__ == '__main__':
    main()
