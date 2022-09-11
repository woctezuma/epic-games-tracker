from src.json_utils import load_json

DATA_FOLDER_NAME = 'data'
SANDBOX_IDS_FNAME = 'sandbox_ids.json'


def load_sandbox_ids_dict():
    return load_json(f"{DATA_FOLDER_NAME}/{SANDBOX_IDS_FNAME}")
