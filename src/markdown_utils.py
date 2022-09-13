from src.fetch_utils import GAME_RATING_FIELDS, ACHIEVEMENT_FIELDS
from src.time_utils import get_current_date_as_str

HEADERS = "| # | Game Slug | Average Rating | Number of Raters | Number of Players | Number of Platinum Trophies | Max Rarity (%) |"
TABLE_SEPARATOR = "|---|---|---|---|---|---|---|"
ENTRY_FIELDS = ['slug'] + GAME_RATING_FIELDS + ACHIEVEMENT_FIELDS


def get_timestamp_line():
    date_as_str = get_current_date_as_str()
    return f"Last updated on {date_as_str}."


def format_data_as_markdown(data):
    lines = [get_timestamp_line(), "\n", HEADERS, TABLE_SEPARATOR]

    for i, entry in enumerate(data.values(), start=1):
        concatenated_entry_values = '|'.join(str(entry[k]) for k in ENTRY_FIELDS)
        line = f"|{i}|{concatenated_entry_values}|"

        lines.append(line)

    return lines
