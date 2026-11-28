from src.utils import create_dummy_dictionary, extract_list_difference, sort_dict_by_key


def test_create_dummy_dictionary():
    assert create_dummy_dictionary(["a", "b"]) == {"a": None, "b": None}


def test_extract_list_difference():
    assert sorted(extract_list_difference(["a", "b", "c"], ["b"])) == ["a", "c"]
    assert extract_list_difference([], ["b"]) == []


def test_sort_dict_by_key():
    assert sort_dict_by_key({"b": 1, "a": 2}) == {"a": 2, "b": 1}
