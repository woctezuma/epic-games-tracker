def sort_dict_by_key(d):
    return dict(sorted(d.items(), key=lambda x: x[0]))
