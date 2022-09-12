from src.json_utils import load_json

DATA_FOLDER_NAME = 'data'
SANDBOX_IDS_FNAME = 'sandbox_ids.json'


def load_sandbox_ids_dict():
    return load_json(f"{DATA_FOLDER_NAME}/{SANDBOX_IDS_FNAME}")


def populate_slugs(data):
    sandbox_ids_dict = load_sandbox_ids_dict()

    for slug, sandbox_id in sandbox_ids_dict.items():
        data[sandbox_id]["slug"] = slug

    return data


def hide_none_elements(data):
    return {k: v for k, v in data.items() if all(e is not None for e in v.values())}
