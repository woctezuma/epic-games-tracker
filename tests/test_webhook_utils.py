from src.webhook_utils import (
    DISCORD_FIXED_TROPHY_HEADER,
    DISCORD_FREE_HEADER,
    DISCORD_LATE_TROPHY_HEADER,
    DISCORD_NEW_HEADER,
    DISCORD_TROPHY_HEADER,
    WEBHOOK_KEYWORD_FIXED_TROPHY,
    WEBHOOK_KEYWORD_FREE,
    WEBHOOK_KEYWORD_LATE_TROPHY,
    WEBHOOK_KEYWORD_NEW,
    WEBHOOK_KEYWORD_TROPHY,
    to_discord_header,
)


def test_to_discord_header_for_known_keywords():
    assert to_discord_header(WEBHOOK_KEYWORD_NEW) == DISCORD_NEW_HEADER
    assert to_discord_header(WEBHOOK_KEYWORD_FREE) == DISCORD_FREE_HEADER
    assert to_discord_header(WEBHOOK_KEYWORD_TROPHY) == DISCORD_TROPHY_HEADER
    assert to_discord_header(WEBHOOK_KEYWORD_LATE_TROPHY) == DISCORD_LATE_TROPHY_HEADER
    assert to_discord_header(WEBHOOK_KEYWORD_FIXED_TROPHY) == DISCORD_FIXED_TROPHY_HEADER


def test_to_discord_header_for_unknown_keyword_is_empty():
    assert to_discord_header("unknown") == ""
