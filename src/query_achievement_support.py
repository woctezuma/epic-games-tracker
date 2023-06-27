from src.api import send_post_request_to_api
from src.query_utils import format_params_for_query_str

def get_params_to_query_achievement_support(sandbox_id):
    query_str = "{Achievement {productAchievementsRecordBySandbox"
    query_str += format_params_for_query_str(sandbox_id)
    query_str += "{"
    query_str += "totalAchievements"
    query_str += "}}}"

    params = {"query": query_str}

    return params


def to_achievement_support(sandbox_id, verbose=True):
    params = get_params_to_query_achievement_support(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        achievement = data["data"]["Achievement"]["productAchievementsRecordBySandbox"]
    except (TypeError, KeyError) as e:
        achievement = None
    return achievement
