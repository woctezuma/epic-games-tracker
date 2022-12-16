from pathlib import Path

from src.data_utils import PAGE_SLUGS_FNAME, UPDATED_DATES_FNAME
from src.data_utils import load_all_updated_dates
from src.download_utils import download_page_slugs, download_updated_dates
from src.json_utils import save_json, load_json
from src.utils import sort_dict_by_key


def main():
    force_update = True

    if force_update or not Path(PAGE_SLUGS_FNAME).exists():
        print('Updating page slugs.')
        page_slugs = download_page_slugs(include_dlc=False)
        save_json(sorted(page_slugs), PAGE_SLUGS_FNAME, prettify=True)
    else:
        page_slugs = load_json(PAGE_SLUGS_FNAME)

    print('Downloading all updated dates.')
    updated_dates = download_updated_dates(page_slugs, known_updated_dates=load_all_updated_dates())
    save_json(sort_dict_by_key(updated_dates), UPDATED_DATES_FNAME, prettify=True)

    return


if __name__ == '__main__':
    main()
