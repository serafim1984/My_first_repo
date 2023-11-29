def make_request(keys, values):

    if len(keys) != len(values):

        dictionary = {}

        return dictionary

    dictionary = dict(zip(keys, values))

    return dictionary