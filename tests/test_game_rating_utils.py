from src.game_rating_utils import compute_rating_count, get_poll_totals


def test_get_poll_totals():
    data_element = {"pollResult": [{"total": 5}, {"total": 9}]}
    assert get_poll_totals(data_element) == [5, 9]


def test_get_poll_totals_with_missing_poll_result():
    assert get_poll_totals({"pollResult": None}) == []


def test_compute_rating_count_takes_the_max_total():
    data_element = {"pollResult": [{"total": 5}, {"total": 9}, {"total": 3}]}
    assert compute_rating_count(data_element) == 9


def test_compute_rating_count_with_no_poll_result():
    assert compute_rating_count({"pollResult": None}) is None
    assert compute_rating_count({"pollResult": []}) is None
