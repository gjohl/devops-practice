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
    greeting_string = ", ".join(['Hello', name])
    print(greeting_string)

    return greeting_string

