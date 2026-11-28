from src.page_mapping_utils import filter_page_mappings_based_on_slugs, get_sandbox_id


def test_get_sandbox_id():
    assert get_sandbox_id({"sandboxId": "abc123"}) == "abc123"


def test_filter_page_mappings_based_on_slugs():
    page_mappings = {"game-a": "id-a", "game-b": "id-b", "game-c": "id-c"}
    filtered = filter_page_mappings_based_on_slugs(page_mappings, {"game-a", "game-c"})
    assert filtered == {"game-a": "id-a", "game-c": "id-c"}
