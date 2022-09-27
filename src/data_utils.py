from src.game_rating_utils import compute_rating_count
from src.json_utils import load_json

DATA_FOLDER_NAME = 'data'
SANDBOX_IDS_FNAME = 'sandbox_ids.json'
PAGE_MAPPINGS_FNAME = 'page_mappings.json'


def load_sandbox_ids_dict():
    return load_json(f"{DATA_FOLDER_NAME}/{SANDBOX_IDS_FNAME}")


def load_all_sandbox_ids_dict():
    try:
        data = load_json(f"{DATA_FOLDER_NAME}/{PAGE_MAPPINGS_FNAME}")
    except FileNotFoundError:
        data = {}

    return data


def populate_slugs(data):
    sandbox_ids_dict = load_sandbox_ids_dict()

    for slug, sandbox_id in sandbox_ids_dict.items():
        data[sandbox_id]["slug"] = slug

    return data


def populate_rating_counts(data):
    for sandbox_id, v in data.items():
        data[sandbox_id]["ratingCount"] = compute_rating_count(v)

    return data
