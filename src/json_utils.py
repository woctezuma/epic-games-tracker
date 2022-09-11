import json


def load_json(fname):
    with open(fname, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def save_json(data, fname):
    with open(fname, 'w', encoding='utf8') as f:
        json.dump(data, f)
