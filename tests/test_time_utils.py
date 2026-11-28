import re
from datetime import UTC, datetime

from src.time_utils import (
    get_current_date_as_str,
    get_fname_for_specific_day,
    get_folder_name_for_specific_day,
)


def test_folder_name_for_specific_day():
    date = datetime(2025, 7, 3, tzinfo=UTC)
    assert get_folder_name_for_specific_day(date) == "data/2025/07"


def test_fname_for_specific_day():
    date = datetime(2025, 12, 31, tzinfo=UTC)
    assert get_fname_for_specific_day(date) == "data/2025/12/31.json"


def test_current_date_as_str_format():
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", get_current_date_as_str())
