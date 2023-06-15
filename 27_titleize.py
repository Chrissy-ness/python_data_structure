def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    
    lower_cased = phrase.lower().split()
    final_phrase = []
    for word in lower_cased:
        final_phrase.append(word.capitalize())
    
    return " ".join(final_phrase)