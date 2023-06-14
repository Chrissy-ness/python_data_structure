def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """

    temp_list_a = []
    temp_list_b = []
    result_a = None
    result_b = None

    final = False

    for item in a:
        if type(item) == list:
            result_a = temp_list_a + item
        else:
            temp_list_a.append(item)

    for item in b:
        if type(item) == list:
            result_b = temp_list_b + item
        else:
            temp_list_b.append(item)

    for el in result_a:
        if el in result_b:
            final = True

    return final





    