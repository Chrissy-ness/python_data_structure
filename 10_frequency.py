def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    freq_num = 0
    for item in lst:
        if item == search_term:
            freq_num += 1
    
    return freq_num