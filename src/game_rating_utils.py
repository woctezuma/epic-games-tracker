def get_poll_results(data_element):
    return data_element['pollResult']


def get_poll_totals(data_element):
    poll_results = get_poll_results(data_element)

    if poll_results is not None:
        poll_totals = [e['total'] for e in poll_results]
    else:
        poll_totals = []

    return poll_totals


def compute_rating_count(data_element):
    poll_totals = get_poll_totals(data_element)

    if len(poll_totals) > 0:
        rating_count = max(poll_totals)
    else:
        rating_count = None

    return rating_count
