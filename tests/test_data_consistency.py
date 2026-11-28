import pytest

from src.data_consistency import has_consistent_stats


def make_valid_entry():
    return {
        "averageRating": 4.5,
        "ratingCount": 100,
        "numProgressed": 50,
        "numCompleted": 10,
        "maxRarity": 25,
    }


def test_valid_entry_is_consistent():
    assert has_consistent_stats(make_valid_entry())


@pytest.mark.parametrize(
    "field,value",
    [
        ("averageRating", 0),
        ("averageRating", 6),
        ("ratingCount", -1),
        ("numProgressed", -1),
        ("numCompleted", 51),  # greater than numProgressed
        ("maxRarity", -1),
        ("maxRarity", 101),
        ("averageRating", None),
        ("numProgressed", None),
        ("numCompleted", None),
        ("maxRarity", None),
    ],
)
def test_inconsistent_entries_are_rejected(field, value):
    entry = make_valid_entry()
    entry[field] = value
    assert not has_consistent_stats(entry)


def test_zero_num_completed_is_consistent():
    entry = make_valid_entry()
    entry["numCompleted"] = 0
    assert has_consistent_stats(entry)
