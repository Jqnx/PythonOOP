def add(a, b):
    """
    Add b to a
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a
    """
    return a - b


def multiply(a, b):
    """
    Multiply a with b
    """
    return a * b


def divide(a, b):
    """
    Deel a door b

    Parameters:
        a: teller
        b: noemer

    Returns:
        float: Resulaat van deling

    Raises:
        ZeroDivisionError: Als b gelijk is aan 0
    """
    if b == 0:
        raise ZeroDivisionError("Kan niet delen door nul")
    return a / b
