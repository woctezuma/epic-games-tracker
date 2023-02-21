from datetime import timedelta

from src.achievement_fixes import list_slugs_with_fixed_achievements
from src.json_utils import load_json, load_json_failsafe
from src.time_utils import get_fname_for_specific_day, get_current_date


def display_results(date, game_slugs):
    print(date.strftime('%Y-%m-%d'))
    print('- ' + '\n- '.join(game_slugs))
    print()


def main():
    date = get_current_date()

    while True:
        data_today = load_json(fname=get_fname_for_specific_day(date))
        data_yesterday = load_json_failsafe(fname=get_fname_for_specific_day(date - timedelta(days=1)))

        if len(data_yesterday) == 0:
            break

        game_slugs = list_slugs_with_fixed_achievements(data_yesterday, data_today)

        if len(game_slugs) > 0:
            display_results(date, game_slugs)

        date -= timedelta(days=1)


if __name__ == '__main__':
    main()
