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
