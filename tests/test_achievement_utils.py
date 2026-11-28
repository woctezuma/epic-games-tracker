from src.achievement_utils import (
    compute_max_unlock_percentage,
    get_main_achievement_set,
    summarize_achievement,
)


def make_achievement_data(percents, sets):
    return {
        "achievements": [{"achievement": {"rarity": {"percent": p}}} for p in percents],
        "achievementSets": sets,
    }


def test_compute_max_unlock_percentage():
    data = make_achievement_data([10, 42, 7], sets=[])
    assert compute_max_unlock_percentage(data) == 42


def test_compute_max_unlock_percentage_with_no_achievement():
    assert compute_max_unlock_percentage(make_achievement_data([], sets=[])) is None


def test_main_achievement_set_prefers_base_sets():
    base = {"isBase": True, "numProgressed": "10"}
    dlc = {"isBase": False, "numProgressed": "999"}
    data = make_achievement_data([], sets=[dlc, base])
    assert get_main_achievement_set(data) is base


def test_main_achievement_set_picks_most_players_among_base_sets():
    small = {"isBase": True, "numProgressed": "10"}
    big = {"isBase": True, "numProgressed": "999"}
    data = make_achievement_data([], sets=[small, big])
    assert get_main_achievement_set(data) is big


def test_main_achievement_set_falls_back_to_all_sets():
    only_dlc = {"isBase": False, "numProgressed": "10"}
    data = make_achievement_data([], sets=[only_dlc])
    assert get_main_achievement_set(data) is only_dlc


def test_summarize_achievement_adds_max_rarity():
    base = {"isBase": True, "numProgressed": "10"}
    data = make_achievement_data([5, 30], sets=[base])
    summary = summarize_achievement(data)
    assert summary["numProgressed"] == "10"
    assert summary["maxRarity"] == 30
