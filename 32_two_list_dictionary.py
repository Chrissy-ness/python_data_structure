def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """
    diction = {}
    x = 0


    if len(keys) <= len(values):
        for key in keys:
            diction[key] = values[x]
            x += 1
        
        return diction

    elif len(keys) > len(values):
        for key in keys:
            diction[key] = None
        
        for x in range(len(values)):
            diction[keys[x]] = values[x]

        return diction
