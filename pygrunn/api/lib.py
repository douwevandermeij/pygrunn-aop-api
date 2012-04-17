
# extract the items of a dict (dict) with keys that are provided in a list (keys)
extract = lambda keys, dict: reduce(lambda x, y: x.update({y[0]:y[1]}) or x,
    map(None, keys, map(dict.get, keys)), {})
