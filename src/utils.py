import operator


def sort_dict_by_key(d):
    return dict(sorted(d.items(), key=operator.itemgetter(0)))


def extract_list_difference(new_list, old_list):
    return list(set(new_list).difference(old_list))


def create_dummy_dictionary(field):
    return {s: None for s in field}
