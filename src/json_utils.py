import json
from pathlib import Path


def load_json(fname):
    with Path(fname).open(encoding='utf8') as f:
        data = json.load(f)
    return data


def load_json_failsafe(fname):
    try:
        data = load_json(fname)
    except FileNotFoundError:
        data = {}
    return data


def save_json(data, fname, prettify=False, indent=4) -> None:
    with Path(fname).open('w', encoding='utf8') as f:
        if prettify:
            json.dump(data, f, indent=indent)
        else:
            json.dump(data, f)
