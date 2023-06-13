def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    final_phrase = []
    check_casing = to_swap.islower()


    for ltr in phrase:
        if check_casing == True:
            if ltr == to_swap:
                final_phrase.append(ltr.upper())
            elif ltr == to_swap.upper():
                final_phrase.append(ltr.lower())
            else:
                final_phrase.append(ltr)
        elif check_casing == False:
            # this means the swap value is capitalized
            if ltr == to_swap:
                final_phrase.append(ltr.lower())
            elif ltr == to_swap.lower():
                final_phrase.append(ltr.upper())
            else:
                final_phrase.append(ltr)

    return "".join(final_phrase)
            
            
        
        
        




    