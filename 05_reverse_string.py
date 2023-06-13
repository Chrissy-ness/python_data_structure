def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_list = list(phrase)
    new_list.reverse()
    
    return "".join(new_list)