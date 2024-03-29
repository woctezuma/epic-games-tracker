import logging
from pathlib import Path

from src.data_filters import (
    hide_games_missing_a_stat,
    hide_games_with_buggy_achievements,
    hide_games_with_inconsistent_stats,
    hide_games_with_zero_player,
)
from src.data_utils import (
    load_tracked_page_mappings,
    populate_rating_counts,
    populate_slugs,
)
from src.export_utils import write_markdown_files
from src.fetch_utils import fetch_data_for_several_ids
from src.json_utils import load_json, save_json
from src.time_utils import get_fname_for_today


def main() -> None:
    logging.getLogger('backoff').addHandler(logging.StreamHandler())

    output_fname = get_fname_for_today()
    Path(output_fname).parent.mkdir(parents=True, exist_ok=True)

    requires_to_download_json = not Path(output_fname).exists()
    requires_to_update_markdown = requires_to_download_json

    if requires_to_download_json:
        print('Updating JSON.')
        sandbox_ids_dict = load_tracked_page_mappings()
        data = fetch_data_for_several_ids(sandbox_ids=sandbox_ids_dict.values())
        save_json(data, output_fname, prettify=True, indent=2)
    else:
        data = load_json(output_fname)

    if requires_to_update_markdown:
        print('Updating Markown.')
        data = populate_slugs(data)
        data = populate_rating_counts(data)
        data = hide_games_missing_a_stat(data)
        data = hide_games_with_inconsistent_stats(data)
        data = hide_games_with_zero_player(data)
        data = hide_games_with_buggy_achievements(data)
        write_markdown_files(data)


if __name__ == '__main__':
    main()
