import operator

get_poll_results = operator.itemgetter('pollResult')


def get_poll_totals(data_element):
    poll_results = get_poll_results(data_element)

    poll_totals = [e['total'] for e in poll_results] if poll_results is not None else []

    return poll_totals


def compute_rating_count(data_element):
    poll_totals = get_poll_totals(data_element)

    rating_count = max(poll_totals) if len(poll_totals) > 0 else None

    return rating_count
