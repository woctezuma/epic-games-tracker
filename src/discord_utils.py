import requests

from src.api import TIMEOUT_IN_SECONDS
from src.data_utils import load_discord_webhook
from src.git_utils import extract_new_games, git_diff
from src.webhook_utils import to_discord_header

BULLET_POINT_SEPARATOR = "\n- "
STORE_URL = "https://epicgames.com/p/"


def to_hyperlink(game_slug: str) -> str:
    return f"[`{game_slug}`]({STORE_URL}{game_slug})"


def to_hyperlinks(game_slugs: list[str]) -> list[str]:
    return [to_hyperlink(game_slug) for game_slug in game_slugs if game_slug]


def get_webhook_id(webhook_keyword='id'):
    webhook = load_discord_webhook()
    try:
        webhook_id = webhook[webhook_keyword]
    except KeyError:
        webhook_id = None
    return webhook_id


def get_webhook_url(webhook_id) -> str:
    return f"https://discord.com/api/webhooks/{webhook_id}"


def post_message_to_discord(message, webhook_id):
    if webhook_id is None or len(message) == 0:
        response = None
    else:
        discord_url = get_webhook_url(webhook_id)
        json_data = {"content": message}
        response = requests.post(
            url=discord_url, json=json_data, timeout=TIMEOUT_IN_SECONDS
        )

    return response


def format_discord_message(games, header="", *, turn_into_hyperlinks: bool = False):
    if turn_into_hyperlinks:
        games = to_hyperlinks(games)
    if len(games) > 0:
        lines = [header, *sorted(games)]
        message = BULLET_POINT_SEPARATOR.join(lines)
    else:
        message = ''
    return message


def post_git_diff_to_discord(fname, header, webhook_id=None):
    if webhook_id is None:
        webhook_id = get_webhook_id()

    stdout, stderr = git_diff(fname)
    games = extract_new_games(stdout)

    message = format_discord_message(games, header=header)
    response = post_message_to_discord(message, webhook_id)

    return response


def post_git_diff_to_discord_using_keyword(fname, webhook_keyword):
    header = to_discord_header(webhook_keyword)
    webhook_id = get_webhook_id(webhook_keyword)
    return post_git_diff_to_discord(fname, header, webhook_id=webhook_id)


def post_slugs_to_discord(game_slugs, webhook_keyword):
    header = to_discord_header(webhook_keyword)
    webhook_id = get_webhook_id(webhook_keyword)

    message = format_discord_message(game_slugs, header=header)
    response = post_message_to_discord(message, webhook_id=webhook_id)

    return response
