import src.data_utils
from src.data_utils import populate_rating_counts, populate_slugs


def test_populate_rating_counts():
    data = {"id-a": {"pollResult": [{"total": 3}, {"total": 7}]}}
    populate_rating_counts(data)
    assert data["id-a"]["ratingCount"] == 7


def test_populate_slugs(monkeypatch):
    monkeypatch.setattr(
        src.data_utils,
        "load_tracked_page_mappings",
        lambda: {"game-a": "id-a", "game-missing": "id-x"},
    )
    data = {"id-a": {}}
    populate_slugs(data)
    assert data["id-a"]["slug"] == "game-a"
