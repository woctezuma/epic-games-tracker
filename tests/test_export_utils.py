import src.export_utils
from src.export_utils import deal_with_none, write_lines_to_disk, write_markdown_files


def make_entry(slug, num_players):
    return {
        "slug": slug,
        "averageRating": 4.0,
        "ratingCount": 10,
        "numProgressed": num_players,
        "numCompleted": 1,
        "maxRarity": 5,
    }


def test_deal_with_none():
    assert deal_with_none(None) == 0
    assert deal_with_none(None, min_value=1) == 1
    assert deal_with_none(0) == 0
    assert deal_with_none(5) == 5


def test_write_lines_to_disk(tmp_path):
    fname = tmp_path / "out.md"
    write_lines_to_disk(["a", "b"], fname)
    assert fname.read_text(encoding="utf8") == "a\nb\n"


def test_write_markdown_files_creates_six_sorted_tables(tmp_path, monkeypatch):
    monkeypatch.setattr(src.export_utils, "OUTPUT_FOLDER", str(tmp_path))

    data = {
        "id-a": make_entry("game-a", num_players=100),
        "id-b": make_entry("game-b", num_players=5000),
    }
    write_markdown_files(data)

    expected_files = [
        "by_game_slug.md",
        "by_average_rating.md",
        "by_num_raters.md",
        "by_num_players.md",
        "by_num_platinum_trophies.md",
        "by_max_rarity.md",
    ]
    for fname in expected_files:
        assert (tmp_path / fname).exists()

    by_slug = (tmp_path / "by_game_slug.md").read_text(encoding="utf8")
    assert by_slug.index("game-a") < by_slug.index("game-b")

    by_players = (tmp_path / "by_num_players.md").read_text(encoding="utf8")
    assert by_players.index("game-b") < by_players.index("game-a")
