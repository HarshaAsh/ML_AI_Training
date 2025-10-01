def middle_of_three(a, b, c):
    """
    Returns the middle one of three numbers a,b,c
    Examples:
    >>> middle_of_three(5, 3, 4)
    4
    >>> middle_of_three(1, 1, 2)
    1
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    lis = [a,b,c]
    lis.sort()
    return lis[1]


def sum_up_to(n):
    """
    Returns the sum of integers from 1 to n
    
    Examples:
    >>> sum_up_to(1)
    1
    >>> sum_up_to(5)
    15
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    i=0
    sum= 0
    while(i<=n):
        sum = i+sum
        i+=1
    return sum


def square_root_heron(x, epsilon=0.01):
    """
    Find square root using Heron's algorithm

    Parameters:
    x: integer or float
    epsilon: desired precision,
        default value epsilon = 0.01 if not specified

    Returns:
    the square root value, rounded to two decimals
    the number of iterations of the algorithm run

    Example use:
    >>> y, c = square_root_heron(20)
    >>> print(y, c)
    4.47 4
    """
    # DON'T CHANGE ANYTHING ABOVE
    # UPDATE CODE BELOW
    
    guess = x/2 # Make initial guess
    # Loop until squared value of guess is close to x
    i=0
    while abs(guess*guess - x) >= epsilon:
        guess = (guess + x/guess)/2 # Update guess using Heron's formula
        i+=1
    return round(guess, 2), i # replace the dots with the final number of iterations


def square_root_bisection(x, epsilon=0.01):
    """
    Find square root using bisection search

    Parameters:
    x: integer or float
    epsilon: desired precision,
        default value epsilon = 0.01 if not specified

    Returns:
    the square root value, rounded to two decimals
    the number of iterations of the algorithm run

    Example use:
    >>> y, c = square_root_bisection(20)
    >>> print(y, c)
    4.47 9
    """
    # DON'T CHANGE ANYTHING ABOVE
    # UPDATE CODE BELOW
    i=0
    low = 0.0
    high = max(1.0, x) # Why are we doing this? What would happen for x=0.5?
    guess = (low + high)/2 # First guess at midpoint of low and high
    while abs(guess*guess - x) >= epsilon:
        if guess*guess < x:
            low = guess # update low
        else:
            high = guess # update high
        guess = (low + high)/2 # new guess at midpoint of low and high
        i+=1
    return round(guess, 2), i


for i in [0.1, 0.2, 0.25, 0.5, 1, 2, 2.5, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000]:
    y_heron, c_heron = square_root_heron(i)
    y_bisection, c_bisection = square_root_bisection(i)
    print(i,y_heron,y_bisection,c_heron,c_bisection)


