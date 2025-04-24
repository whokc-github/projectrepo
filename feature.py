def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    Args:
        a (int, float): First number to add
        b (int, float): Second number to add
    Returns:
        int or float: Sum of a and b
    """
    try:
        return a + b
    except TypeError:
        raise TypeError("Both arguments must be numbers (int or float)")
