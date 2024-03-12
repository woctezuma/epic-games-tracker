from src.game_rating_utils import compute_rating_count
from src.json_utils import load_json_failsafe

DATA_FOLDER_NAME = 'data'
JSON_SUFFIX = 'json'
SANDBOX_IDS_FNAME = f'{DATA_FOLDER_NAME}/sandbox_ids.{JSON_SUFFIX}'
PAGE_MAPPINGS_FNAME = f'{DATA_FOLDER_NAME}/page_mappings.{JSON_SUFFIX}'
PAGE_SLUGS_FNAME = f'{DATA_FOLDER_NAME}/page_slugs.{JSON_SUFFIX}'
DISCORD_WEBHOOK_FNAME = f'{DATA_FOLDER_NAME}/discord_webhook.{JSON_SUFFIX}'


def load_tracked_page_mappings():
    return load_json_failsafe(SANDBOX_IDS_FNAME)


def load_all_page_mappings():
    return load_json_failsafe(PAGE_MAPPINGS_FNAME)


def load_discord_webhook():
    return load_json_failsafe(DISCORD_WEBHOOK_FNAME)


def populate_slugs(data):
    sandbox_ids_dict = load_tracked_page_mappings()

    for slug, sandbox_id in sandbox_ids_dict.items():
        try:
            data[sandbox_id]["slug"] = slug
        except KeyError:
            continue

    return data


def populate_rating_counts(data):
    for sandbox_id, v in data.items():
        data[sandbox_id]["ratingCount"] = compute_rating_count(v)

    return data
