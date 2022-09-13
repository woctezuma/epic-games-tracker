from src.fetch_utils import GAME_RATING_FIELDS, ACHIEVEMENT_FIELDS
from src.time_utils import get_current_date_as_str

GAME_RATING_HEADERS = ["Average Rating", "Number of Raters"]
ACHIEVEMENT_HEADERS = ["Number of Players", "Number of Platinum Trophies", "Max Rarity (%)"]
HEADERS = ["Game Slug"] + GAME_RATING_HEADERS + ACHIEVEMENT_HEADERS
TABLE_SEPARATOR = "|---|---|---|---|---|---|---|"
ENTRY_FIELDS = ['slug'] + GAME_RATING_FIELDS + ACHIEVEMENT_FIELDS


def get_timestamp_line():
    date_as_str = get_current_date_as_str()
    return f"Last updated on {date_as_str}."


def to_table_row(row_no, str_elements):
    concatenated_elements = '|'.join(str_elements)
    line = f"|{row_no}|{concatenated_elements}|"
    return line


def get_headers_line():
    place_holder_for_number = '#'
    return to_table_row(place_holder_for_number, HEADERS)


def format_data_as_markdown(data):
    lines = [get_timestamp_line(), "\n", get_headers_line(), TABLE_SEPARATOR]

    for i, entry in enumerate(data.values(), start=1):
        line = to_table_row(i, [str(entry[k]) for k in ENTRY_FIELDS])

        lines.append(line)

    return lines
