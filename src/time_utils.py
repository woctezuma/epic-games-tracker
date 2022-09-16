from datetime import datetime

from src.data_utils import DATA_FOLDER_NAME


def get_current_date():
    return datetime.now()


def get_folder_name_for_specific_day(date):
    return f"{DATA_FOLDER_NAME}/{date.year}/{date.month:02}"


def get_fname_for_specific_day(date):
    folder_name = get_folder_name_for_specific_day(date)
    return f"{folder_name}/{date.day:02}.json"


def get_fname_for_today():
    date = get_current_date()
    return get_fname_for_specific_day(date)
