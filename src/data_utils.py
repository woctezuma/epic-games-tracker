from src.game_rating_utils import compute_rating_count
from src.json_utils import load_json

DATA_FOLDER_NAME = 'data'
SANDBOX_IDS_FNAME = f'{DATA_FOLDER_NAME}/sandbox_ids.json'
PAGE_MAPPINGS_FNAME = f'{DATA_FOLDER_NAME}/page_mappings.json'


def load_tracked_page_mappings():
    return load_json(f"{SANDBOX_IDS_FNAME}")


def load_all_page_mappings():
    try:
        data = load_json(f"{PAGE_MAPPINGS_FNAME}")
    except FileNotFoundError:
        data = {}

    return data


def populate_slugs(data):
    sandbox_ids_dict = load_tracked_page_mappings()

    for slug, sandbox_id in sandbox_ids_dict.items():
        data[sandbox_id]["slug"] = slug

    return data


def populate_rating_counts(data):
    for sandbox_id, v in data.items():
        data[sandbox_id]["ratingCount"] = compute_rating_count(v)

    return data
