from src.fields import (
    ACHIEVEMENT_FIELDS,
    ACHIEVEMENT_HEADERS,
    GAME_RATING_FIELDS,
    GAME_RATING_HEADERS,
)
from src.time_utils import get_current_date_as_str

HEADERS = ["Game Slug", *GAME_RATING_HEADERS, *ACHIEVEMENT_HEADERS]
ENTRY_FIELDS = ["slug", *GAME_RATING_FIELDS, *ACHIEVEMENT_FIELDS]
PLACE_HOLDER = '---'
PLACE_HOLDER_FOR_NUMBER = '#'


def get_timestamp_line() -> str:
    date_as_str = get_current_date_as_str()
    return f"Last updated on {date_as_str}."


def to_table_row(row_no, str_elements):
    concatenated_elements = '|'.join(str_elements)
    line = f"|{row_no}|{concatenated_elements}|"
    return line


def get_headers_line():
    return to_table_row(PLACE_HOLDER_FOR_NUMBER, HEADERS)


def get_separator_line():
    place_holder = PLACE_HOLDER
    num_headers = len(HEADERS)
    return to_table_row(place_holder, [place_holder] * num_headers)


def format_data_as_markdown(data, number_rows=False):
    lines = [get_timestamp_line(), "\n", get_headers_line(), get_separator_line()]

    for i, entry in enumerate(data.values(), start=1):
        row_index = i if number_rows else PLACE_HOLDER_FOR_NUMBER
        line = to_table_row(row_index, [str(entry[k]) for k in ENTRY_FIELDS])

        lines.append(line)

    return lines
