from src.achievement_fixes import list_slugs_with_fixed_achievements
from src.json_utils import load_json
from src.time_utils import list_data_file_names
from src.data_utils import JSON_SUFFIX

FNAME_PREFIX = 'data/'
FNAME_SUFFIX = f'.{JSON_SUFFIX}'
FOLDER_SEPARATOR = "/"
DATE_SEPARATOR = "-"


def display_results(date_str, game_slugs) -> None:
    print(date_str)
    print('- ' + '\n- '.join(sorted(game_slugs)))
    print()


def extract_date_from_fname(fname):
    return (
        str(fname)
        .removeprefix(FNAME_PREFIX)
        .removesuffix(FNAME_SUFFIX)
        .replace(FOLDER_SEPARATOR, DATE_SEPARATOR)
    )


def main() -> None:
    all_fnames = list_data_file_names()

    current_fname = None
    for previous_fname in reversed(all_fnames):
        if current_fname is not None:
            data_today = load_json(fname=current_fname)
            data_yesterday = load_json(fname=previous_fname)

            game_slugs = list_slugs_with_fixed_achievements(data_yesterday, data_today)

            if len(game_slugs) > 0:
                date_str = extract_date_from_fname(current_fname)
                display_results(date_str, game_slugs)

        current_fname = previous_fname


if __name__ == '__main__':
    main()
