def item_lengths(input_list):
    """
    Create a list containing the lengths of the items in input_list
    
    Parameters:
        input_list: list
    Returns:
        a list containing lengths of items in input_list
    
    Examples:
    >>> item_lengths(['hello', 'how', 'are', 'you', 'doing'])
    [5, 3, 3, 3, 5]
    >>> item_lengths('All happy families are alike'.split())
    [3, 5, 8, 3, 5]
    >>> x = item_lengths('All happy families are alike'.split())
    >>> x[0]
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    list_of_lengths = []
    for item in input_list:
        list_of_lengths.append(len(item))
    return(list_of_lengths)


def longest_item(input_list):
    """
    Finds the longest item in input_list
    
    Parameters:
        input_list: list
    Returns:
        the index of the longest item in input_list 
        (if there are ties, return the first such index)
    
    Examples:
    >>> longest_item(['hello', 'how', 'are', 'you'])
    0
    >>> longest_item('All happy families are alike'.split())
    2
    >>> x = longest_item('All happy families are alike'.split())
    >>> isinstance(x, int) # check that result is an integer
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    index_of_largest_string = None
    length_of_largest_string  = 0
    counter = 0
    for item in input_list:
        if(len(item)>length_of_largest_string):
            index_of_largest_string = counter
            length_of_largest_string = len(item)
        counter+=1
    return(index_of_largest_string)
    
