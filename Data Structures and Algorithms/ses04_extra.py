def recursive_fibonacci(n):
    """
    Assumes that n is an int >= 0
        returns Fibonacci of n
    
    Example use:
    >>> recursive_fibonacci(2)
    1
    >>> recursive_fibonacci(5)
    5
    >>> recursive_fibonacci(8)
    21
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    if(n==1):
        return 1
    if(n==2):
        return 1
    elif(n>2):
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)
    else:
        return None


def merge_sort(L):
    """
    Sort the input list using the merge sort algorithm.
    
    Parameters:
        L is an unsorted list
        
    Returns:
        L sorted in increasing order
    
    Examples:
    >>> merge_sort([3, 6, 8, 2, 78, 1, 23, 45, 9])
    [1, 2, 3, 6, 8, 9, 23, 45, 78]
    >>> merge_sort([1, 13, -23, 2.7, -3, 5, 7.5])
    [-23, -3, 1, 2.7, 5, 7.5, 13]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    if(len(L)>2):
        splitting_index = len(L)//2
        return merge( merge_sort(L[0:splitting_index]), merge_sort(L[splitting_index:]) )
    elif(len(L)==2):
        if(L[0]>L[1]):
            a = L[1]
            L[1] = L[0]
            L[0] = a
            return(L)
        else:
            return(L)
    else:
        return(L)
        


def merge(left, right):
    """
    Merge two sorted lists into one
    
    Parameters: 
        left and right are sorted lists
       
    Returns a single sorted list.
    
    Example use:
    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    # YOUR CODE BELOW
    # DON'T CHANGE ANYTHING ABOVE
    combined = []
    left_counter = 0
    right_counter=0
    
    while((left_counter<len(left)) and (right_counter<len(right))):
        if(left[left_counter]<right[right_counter]):
            combined.append(left[left_counter])
            left_counter+=1
        elif(left[left_counter]>right[right_counter]):
            combined.append(right[right_counter])
            right_counter+=1
    
    if(left_counter==len(left)):
        combined.extend(right[right_counter:])
    if(right_counter==len(right)):
        combined.extend(left[left_counter:])
    
    return(combined)
        

def check_sorted(L):
    """
    Uses looping to check whether a list is sorted or not (could be increasing or decreasing).
    Examples:
    >>> check_sorted([3, 6, 48, 24, 51, 262, 119])
    False
    >>> check_sorted([748, 623, 424, 414, 74, 2])
    True
    >>> check_sorted([1, 2, 3])
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    sorted_list = merge_sort(L)
    if(sorted_list==L):
        return True
    elif(sorted_list == L[::-1]):
        return True
    else:
        return False


def longest_sorted(L):
    """
    Uses looping to return the longest sorted sequence in a list (ascending).
    Examples:
    >>> longest_sorted([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 13, 15, 3, 11, 7, 5])
    [1, 9, 13, 15]
    >>> longest_sorted([25, 72, 31, 32, 8, 20, 38, 43, 85, 39, 33, 40, 98, 37, 14])
    [8, 20, 38, 43, 85]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    longest_streak_list = L[0]
    longest_streak_time = 0
    local_maxima_longest_streak_list = []
    local_maxima_longest_streak_time = 0
    for el in range(0,len(L)):
        if(L[el]-L[el-1]>=0):
            local_maxima_longest_streak_list.append(L[el-1])
            local_maxima_longest_streak_time +=1
            if(local_maxima_longest_streak_time > longest_streak_time):
                longest_streak_list = list(local_maxima_longest_streak_list)
                longest_streak_list.append(L[el])
                longest_streak_time = local_maxima_longest_streak_time
        else:
            local_maxima_longest_streak_time = 0
            local_maxima_longest_streak_list = []
    return longest_streak_list