#!/usr/bin/python3
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
    tmp_text = text.replace('.', '.\n\n').replace('?', '?\n\n')
    tmp_text = temp.replace(':', ':\n\n')
    tmp_text = tmp_text.split("\n ")
    new_text = []
    for s_text in tmp_text:
        while (s_text[0] == ' ' or s_text[-1] == ' '):
            if s_text[0] == ' ':
                s_text = s_text[1:]
            if s_text[-1] == ' ':
                s_text = s_text[:-1]
            new_text.append(s_text)
    print("\n".join(new_text), end="")
