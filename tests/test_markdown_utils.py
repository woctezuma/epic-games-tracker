from src.markdown_utils import (
    format_data_as_markdown,
    get_headers_line,
    get_separator_line,
    get_timestamp_line,
    to_table_row,
)


def test_timestamp_line():
    assert get_timestamp_line().startswith("Last updated on ")
    assert get_timestamp_line().endswith(".")


def test_headers_line():
    assert get_headers_line() == (
        "|#|Game Slug|Average Rating|Number of Raters"
        "|Number of Players|Number of Platinum Trophies|Max Rarity (%)|"
    )


def test_separator_line():
    assert get_separator_line() == "|---|---|---|---|---|---|---|"


def test_to_table_row():
    assert to_table_row(3, ["a", "b"]) == "|3|a|b|"


def test_format_data_as_markdown():
    entry = {
        "slug": "my-game",
        "averageRating": 4.5,
        "ratingCount": 100,
        "numProgressed": 50,
        "numCompleted": 10,
        "maxRarity": 25,
    }
    lines = format_data_as_markdown({"sandbox-id": entry}, number_rows=True)

    assert lines[0].startswith("Last updated on ")
    assert lines[2] == get_headers_line()
    assert lines[3] == get_separator_line()
    assert lines[4] == "|1|my-game|4.5|100|50|10|25|"
