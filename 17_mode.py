def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    
    temp_dict = {}
    highest_val = 0

    for num in nums:
        if num in temp_dict.keys():
            temp_dict[num] += 1
        else:
            temp_dict[num] = 1
    
    for val in temp_dict.values():
        if val > highest_val:
            highest_val = val

    for key in temp_dict.keys():
        if temp_dict[key] == highest_val:
            return key

        
    
            
    

        
