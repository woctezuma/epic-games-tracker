import json


def load_json(fname):
    with open(fname, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def save_json(data, fname, prettify=False, indent=4):
    with open(fname, 'w', encoding='utf8') as f:
        if prettify:
            json.dump(data, f, indent=indent)
        else:
            json.dump(data, f)
