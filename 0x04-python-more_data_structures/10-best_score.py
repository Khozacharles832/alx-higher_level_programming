def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    _large = None
    _max = float('-inf')
    for key, value in a_dictionary.items():
        if value > _max:
            _large = key
            _max = value
    return (_large)
