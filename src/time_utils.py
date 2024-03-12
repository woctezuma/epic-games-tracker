from datetime import UTC, datetime, timedelta
from pathlib import Path

from src.data_utils import DATA_FOLDER_NAME, JSON_SUFFIX

YEAR_PREFIX = '20'
DATA_FILE_NAME_FORMAT = f'{YEAR_PREFIX}*/*/*.{JSON_SUFFIX}'


def get_current_date():
    return datetime.now(tz=UTC)


def get_current_date_as_str():
    date = get_current_date()
    return str(date)[:16]


def get_folder_name_for_specific_day(date) -> str:
    return f"{DATA_FOLDER_NAME}/{date.year}/{date.month:02}"


def get_fname_for_specific_day(date) -> str:
    folder_name = get_folder_name_for_specific_day(date)
    return f"{folder_name}/{date.day:02}.{JSON_SUFFIX}"


def get_fname_for_yesterday():
    date = get_current_date() - timedelta(days=1)
    return get_fname_for_specific_day(date)


def get_fname_for_today():
    date = get_current_date()
    return get_fname_for_specific_day(date)


def list_data_file_names():
    return sorted(Path(DATA_FOLDER_NAME).glob(DATA_FILE_NAME_FORMAT))


def get_fname_for_the_most_recent_of_past_days():
    all_fnames = list_data_file_names()
    fnames_for_past_days = all_fnames[:-1]
    return fnames_for_past_days[-1]
