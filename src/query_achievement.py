from src.api import send_post_request_to_api


def get_params_to_query_achievement(sandbox_id):
    query_str = "{Achievement {productAchievementsRecordBySandbox"
    query_str += f'(sandboxId: "{sandbox_id}", locale: "en") '
    query_str += "{"
    query_str += "achievementSets {numProgressed numCompleted} achievements {achievement {rarity {percent} } }"
    query_str += "}}}"

    params = {"query": query_str}

    return params


def to_achievement(sandbox_id, verbose=True):
    params = get_params_to_query_achievement(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        achievement = data["data"]["Achievement"]["productAchievementsRecordBySandbox"]
    except (TypeError, KeyError) as e:
        achievement = None
    return achievement
