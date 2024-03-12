from src.api import send_post_request_to_api
from src.query_utils import get_query_str_for_achievements


def get_params_to_query_achievement_support(sandbox_id):
    query_str = "{"
    query_str += get_query_str_for_achievements(
        sandbox_id,
        include_num_achievements=True,
        include_achievement_details=False,
    )
    query_str += "}"

    params = {"query": query_str}

    return params


def to_achievement_support(sandbox_id, verbose=True):
    params = get_params_to_query_achievement_support(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        achievement = data["data"]["Achievement"]["productAchievementsRecordBySandbox"]
    except (TypeError, KeyError):
        achievement = None
    return achievement
