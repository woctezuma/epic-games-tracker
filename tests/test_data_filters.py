from src.data_filters import (
    hide_games_missing_a_stat,
    hide_games_with_buggy_achievements,
    hide_games_with_inconsistent_stats,
    hide_games_with_zero_player,
)


def make_entry(numProgressed=10, numCompleted=5, maxRarity=30, averageRating=4.0, ratingCount=100):
    return {
        "slug": "game",
        "averageRating": averageRating,
        "ratingCount": ratingCount,
        "numProgressed": numProgressed,
        "numCompleted": numCompleted,
        "maxRarity": maxRarity,
    }


def test_hide_games_missing_a_stat():
    data = {"a": make_entry(), "b": make_entry(averageRating=None)}
    assert list(hide_games_missing_a_stat(data)) == ["a"]


def test_hide_games_with_inconsistent_stats():
    data = {"a": make_entry(), "b": make_entry(numCompleted=999)}
    assert list(hide_games_with_inconsistent_stats(data)) == ["a"]


def test_hide_games_with_zero_player():
    data = {"a": make_entry(numProgressed=1), "b": make_entry(numProgressed=0), "c": make_entry(numProgressed=None)}
    assert list(hide_games_with_zero_player(data)) == ["a"]


def test_hide_games_with_buggy_achievements():
    data = {"a": make_entry(maxRarity=1), "b": make_entry(maxRarity=0), "c": make_entry(maxRarity=None)}
    assert list(hide_games_with_buggy_achievements(data)) == ["a"]
