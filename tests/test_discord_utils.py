from src.config import DISCORD_API_URL, STORE_URL
from src.discord_utils import (
    format_discord_message,
    get_webhook_id,
    get_webhook_url,
    post_message_to_discord,
    to_hyperlink,
    to_hyperlinks,
)


def test_to_hyperlink():
    assert to_hyperlink("my-game") == f"[`my-game`]({STORE_URL}my-game)"


def test_to_hyperlinks_filters_out_falsy_slugs():
    assert to_hyperlinks(["a", None, ""]) == [to_hyperlink("a")]


def test_get_webhook_url():
    assert get_webhook_url("123/abc") == f"{DISCORD_API_URL}/123/abc"


def test_get_webhook_id(monkeypatch):
    monkeypatch.setattr(
        "src.discord_utils.load_discord_webhook",
        lambda: {"id": "123", "fix": "456"},
    )
    assert get_webhook_id() == "123"
    assert get_webhook_id("fix") == "456"


def test_get_webhook_id_with_missing_key(monkeypatch):
    monkeypatch.setattr("src.discord_utils.load_discord_webhook", lambda: {})
    assert get_webhook_id() is None


def test_format_discord_message_is_empty_without_games():
    assert format_discord_message([], header="Header") == ""


def test_format_discord_message_sorts_games_as_bullet_points():
    message = format_discord_message(["b-game", "a-game"], header="Header")
    assert message == "Header\n- a-game\n- b-game"


def test_format_discord_message_with_hyperlinks():
    message = format_discord_message(["a-game"], header="Header", turn_into_hyperlinks=True)
    assert message == f"Header\n- {to_hyperlink('a-game')}"


def test_post_message_to_discord_does_nothing_without_webhook_id():
    assert post_message_to_discord("message", webhook_id=None) is None


def test_post_message_to_discord_does_nothing_with_empty_message():
    assert post_message_to_discord("", webhook_id="123") is None
