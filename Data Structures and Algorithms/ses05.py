def print_dict_values(a):
    """
    Prints the key-value pairs of the input dictionary a, sorted based on the key value
    
    Parameters:
        a: dictionary a
        
    Returns:
        the number of keys the input dictionary includes
        
    Examples:
    >>> print_dict_values({'Zoe': 'ICL', 'Mark': 'UCL'})
    Mark UCL
    Zoe ICL
    2
    >>> print_dict_values({'banana': 'yellow', 'apple': 'green', 'berry': 'blue'})
    apple green
    banana yellow
    berry blue
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    keys_ascending = sorted(list(a.keys()))
    for key in keys_ascending:
        print(str(key) + " " + str(a[key]))
    return(len(a))
    
    
def count_characters(a):
    """
    Counts how many times different characters appear in the input string.
    
    Returns: 
        dictionary whose: 
            keys are the characters appearing in the input string a
            values are the counts of the characters in the input string a 
    
    Examples:
    >>> count_characters('aaaa')
    {'a': 4}
    >>> x = count_characters('test')
    >>> print(x['t'])
    2
    >>> x = count_characters('hello')
    >>> print(x['h'])
    1
    >>> x = count_characters('hello world')
    >>> print(x['l'])
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    from collections import defaultdict
    a_dict = defaultdict(lambda:0,{})
    for i in range(len(a)):
        a_dict[a[i]] +=1
    return dict(a_dict)
                


def divide(a, b):
    """
    Divides a by b; catches division by zero
    
    Parameters: 
        a, b: numbers
    
    Returns:
        a divided by b.
        If b is 0, prints out 'No division by 0.' and returns None
    
    Examples
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    No division by 0.
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    try:
        return a/b
    except ZeroDivisionError:
        print('No division by 0.')
        return None


def count_words(a):
    """
    Counts the occurrence of different words in the input string a
    
    Parameters: 
        a: string
    
    Returns: 
        dictionary whose: 
            keys are words
            values are the counts of the words in the input string a 
    
    Examples:
    >>> x = count_words('test sentence')
    >>> print(x['test'])
    1
    >>> x = count_words('it is what it is')
    >>> print(x['it'])
    2
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    from collections import defaultdict
    words_dict = defaultdict(lambda:0,{})
    for i in a.split():
        words_dict[i] +=1
    return dict(words_dict)



