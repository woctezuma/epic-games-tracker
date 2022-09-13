from pathlib import Path

from src.data_filters import hide_games_with_buggy_achievements
from src.data_filters import hide_games_with_none_elements, hide_games_with_zero_player
from src.data_utils import load_sandbox_ids_dict, populate_slugs
from src.export_utils import write_markdown_files
from src.fetch_utils import fetch_data_for_several_ids
from src.json_utils import save_json, load_json
from src.time_utils import get_fname_for_today


def main():
    output_fname = get_fname_for_today()
    Path(output_fname).parent.mkdir(parents=True, exist_ok=True)

    requires_to_download_json = not Path(output_fname).exists()
    requires_to_update_markdown = requires_to_download_json

    if requires_to_download_json:
        print('Updating JSON.')
        sandbox_ids_dict = load_sandbox_ids_dict()
        data = fetch_data_for_several_ids(sandbox_ids=sandbox_ids_dict.values())
        save_json(data, output_fname, prettify=True)
    else:
        data = load_json(output_fname)

    if requires_to_update_markdown:
        print('Updating Markown.')
        data = populate_slugs(data)
        data = hide_games_with_none_elements(data)
        data = hide_games_with_zero_player(data)
        data = hide_games_with_buggy_achievements(data)
        write_markdown_files(data)

    return


if __name__ == '__main__':
    main()
