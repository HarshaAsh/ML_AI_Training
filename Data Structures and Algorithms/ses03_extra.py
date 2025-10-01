#####
# Trump tweets
# Load the csv file first

import csv

def read_trump_tweets(file_name):
    """
    Reads Trump tweets csv file into a list
    
    Parameter:
        file_name: csv file containing the tweets
    
    Returns:
        list containing tweets
    """
    try:
        with open(file_name, encoding="utf8") as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            tweet_list = list(data)
        return tweet_list
    except FileNotFoundError:
        print("""
              File not found. Check that the Spyder working directory is correct.
              Change the working directory by clicking on folder icon in the top right part of the window.
              """)


#####
# String to int

def str_to_int(L, ind):
    """
    Convert string-form integer entries in L to integers. 
    
    Parameters:
        L is a list containing list entries. The first entry contains headers so it is skipped.
        ind is the index at each of the list entries to be converted
        
    Returns a new list with integer entries of the ind entry of each entry of L
    
    Example use:
    >>> L = [['Name', 'Favorites'], ['Jay', '100'], ['Jack', '99']]
    >>> y = str_to_int(L, 1)
    >>> print(y)
    [100, 99]
    >>> L = [['Number1', 'Number2'], ['8', '3'], ['7', '5']]
    >>> y = str_to_int(L, 0)
    >>> print(y)
    [8, 7]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    list_of_int = list()
    for i in range(1, len(L)):
        list_of_int.append(int(L[i][ind]))
    return(list_of_int)


def value_at_least(L, threshold):
    """
    Collects indices of L where value is at least threshold
    
    Parameters:
        L: a list 
        threshold: value threshold
    
    Returns a new list of indices with values at least the threshold
    
    Example use:
    >>> tw = [0, 100, 3]
    >>> value_at_least(tw, 2)
    [1, 2]
    >>> value_at_least([4, 1, 5], 5)
    [2]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    list_of_indices = []
    for i in range(len(L)):
        if(L[i]>=threshold):
            list_of_indices.append(i)
    return list_of_indices


#####
# Applying functions


def apply_function(a_list, function, start_from):
    """
    Applies parameter function to items of a_list. 
    
    Parameters:
        a_list: a list of lists
        function: a function to be applied to each item of a_list,
        start_from: index of a_list to start from
    
    Returns: 
        a new list with the results.
    """
    new_list = []
    for item in a_list[start_from:]:
        new_list.append(function(item))
    return new_list

    
def count_capital_letters(tweet):
    """
    Counts the number of capital numbers of the tweet
    
    Parameters:
        tweet: list containing tweet text in first item
    
    Returns: 
        integer count of the number of capital letters in the tweet text
    
    Example use:
    >>> count_capital_letters(['HEY YOU', 'date1', 100, 10, 'id'])
    6
    >>> count_capital_letters(['hey YOU', 'date1', 100, 10, 'id'])
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    counter=0
    for i in tweet[0]:
        if(i.isupper()):
            counter+=1
    return counter


def to_chars(s):
    """
    Strips the string s from any non-letter characters (English alphabet), 
    and makes it lower-case.
    
    Parameters:
        string s
    Returns: 
        string with only lower-case chars of the English alphabet
        
    Example use
    >>> to_chars('HeLlo!')
    'hello'
    >>> to_chars("Never (1) odd or (2) even...")
    'neveroddoreven'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    alphabet = 'abcdefghjiklmnopqrstuvwxyz' # English alphabet
    char_str = ''
    for char in s:
        if(char.lower() in alphabet):
            char_str = char_str + char.lower()
    return char_str


def is_palindrome(s):
    """ 
    Palindrome checker
    
    Parameters:
        s is string that has gone through to_chars()
    
    Returns True if s is palindrome, False otherwise
    
    Examples:
    >>> is_palindrome('neveroddoreven')
    True
    >>> is_palindrome(to_chars('A man, a plan, a canal: Panama.'))
    True
    >>> is_palindrome('hello')
    False
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    s = to_chars(s)
    for i in range(len(s)):
        if(s[i]!=s[-i-1]):
            return False
    return True


def search_word(s1, s2):
    """
    Finds the longest substring of s1 that is also in s2
    
    Parameters: 
        s1, s2 - strings
    
    Returns: 
        the longest substring of s1 also contained in s2
   
    Examples:
    >>> search_word("searching for a substring", "subway")
    'sub'
    >>> search_word("dog owner", "catdog oh catdog")
    'dog o'
    >>> search_word("fish", "filet")
    'fi'
    >>> search_word("fish", "ballet")
    ''
    >>> search_word("land a plane", "lane")
    'lane'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    # Inspired from https://stackoverflow.com/questions/18715688/find-common-substring-between-two-strings
    longest_substring = ""
    len_1, len_2 = len(s1), len(s2)
    for i in range(len_1):
        for j in range(len_2):
            temp = 0
            max_match = ""
            while(i+temp<len_1 and (j+temp<len_2) and s1[i+temp] == s2[j+temp]):
                 max_match += s2[j+temp]
                 temp+=1
            if (len(max_match) > len(longest_substring)): 
                longest_substring = max_match
    return longest_substring
        