from src.json_utils import load_json, load_json_failsafe, save_json


def test_save_and_load_json_roundtrip(tmp_path):
    fname = tmp_path / "data.json"
    data = {"a": 1, "b": [1, 2, 3]}
    save_json(data, fname)
    assert load_json(fname) == data


def test_save_json_prettify(tmp_path):
    fname = tmp_path / "data.json"
    save_json({"a": 1}, fname, prettify=True, indent=2)
    assert fname.read_text(encoding="utf8") == '{\n  "a": 1\n}'


def test_load_json_failsafe_returns_empty_dict_for_missing_file(tmp_path):
    assert load_json_failsafe(tmp_path / "missing.json") == {}
