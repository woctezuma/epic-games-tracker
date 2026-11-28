from src.git_utils import (
    extract_games,
    extract_new_games,
    filter_additions,
    filter_deletions,
)

SAMPLE_DIFF = """diff --git a/data/sandbox_ids.json b/data/sandbox_ids.json
index 1111111..2222222 100644
--- a/data/sandbox_ids.json
+++ b/data/sandbox_ids.json
@@ -1,3 +1,4 @@
     "game-a": "id-a",
+    "game-b": "id-b",
-    "game-c": "id-c",
"""


def test_filter_additions():
    assert filter_additions(SAMPLE_DIFF) == ['+    "game-b": "id-b",']


def test_filter_deletions():
    assert filter_deletions(SAMPLE_DIFF) == ['-    "game-c": "id-c",']


def test_extract_games():
    assert extract_games(['+    "game-b": "id-b",']) == ["game-b"]
    assert extract_games(["a line without quotes"]) == []


def test_extract_new_games_removes_deleted_games():
    assert extract_new_games(SAMPLE_DIFF) == ["game-b"]


def test_extract_new_games_with_a_game_replaced():
    diff = '+    "game-a": "id-new",\n-    "game-a": "id-old",'
    assert extract_new_games(diff) == []
