def format_params_for_query_str(sandbox_id):
    params_str = f'(sandboxId: "{sandbox_id}", locale: "en") '
    return params_str


def get_query_str_for_achievements(sandbox_id):
    query_str = "Achievement {productAchievementsRecordBySandbox"
    query_str += format_params_for_query_str(sandbox_id)
    query_str += "{"
    query_str += "totalAchievements "
    query_str += "achievementSets {isBase numProgressed numCompleted} achievements {achievement {rarity {percent} } }"
    query_str += "}} "

    return query_str


def get_query_str_for_ratings(sandbox_id):
    query_str = "RatingsPolls {getProductResult"
    query_str += format_params_for_query_str(sandbox_id)
    query_str += "{"
    query_str += "averageRating pollResult {id total}"
    query_str += "}} "

    return query_str
