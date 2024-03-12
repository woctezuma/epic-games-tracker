from src.achievement_fixes import list_slugs_with_fixed_achievements
from src.discord_utils import post_slugs_to_discord
from src.json_utils import load_json, load_json_failsafe
from src.time_utils import (
    get_fname_for_the_most_recent_of_past_days,
    get_fname_for_today,
    get_fname_for_yesterday,
)
from src.webhook_utils import WEBHOOK_KEYWORD_FIXED_TROPHY


def main() -> None:
    try:
        data_yesterday = load_json(fname=get_fname_for_yesterday())
    except FileNotFoundError:
        data_yesterday = load_json_failsafe(fname=get_fname_for_the_most_recent_of_past_days())
    data_today = load_json(fname=get_fname_for_today())

    game_slugs = list_slugs_with_fixed_achievements(data_yesterday, data_today)

    post_slugs_to_discord(game_slugs, webhook_keyword=WEBHOOK_KEYWORD_FIXED_TROPHY)


if __name__ == '__main__':
    main()
