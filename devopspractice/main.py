from devopspractice.utils.exceptions import BadInputError


def greeting(name):
    """
    A function to greet our user.

    Parameters
    ----------
    name: str
        The name of our user

    Returns
    -------
    greeting_string: str
        The greeting to our user
    """
    if not name:
        raise BadInputError("Input must not be empty")

    if len(name) < 3:
        raise BadInputError("Input must have at least 3 characters")

    greeting_string = ", ".join(['Hello', name])
    print(greeting_string)

    return greeting_string


def string_len(input_string):
    """
    Calculate the length of an input string.

    Parameters
    ----------
    input_string: str
        The string to check the length of.

    Returns
    -------
    int
        The number of characters in the input string
    """
    if not isinstance(input_string, str):
        raise BadInputError("Input must be a string")

    return len(input_string)
