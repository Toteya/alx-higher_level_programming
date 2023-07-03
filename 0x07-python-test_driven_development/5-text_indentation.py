""" Module 5-text_indentation
Contains the text_indenation() function
"""


def text_indentation(text):
    """ Prints a text and two new lines after each of the characters
    '.' '?' and ':'

    Args:
        text (str): The string to be printed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace(".", ".\n\n")
    new_text = new_text.replace("?", "?\n\n")
    new_text = new_text.replace(":", ":\n\n")
    new_text = new_text.replace(" \n", "\n")
    new_text = new_text.replace("\n ", "\n")
    print(new_text, end="")
