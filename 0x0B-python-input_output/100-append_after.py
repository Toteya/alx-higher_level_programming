#!/usr/bin/python3
""" Module 100-append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text after each line containing the specified
    string

    Args:
        filname (str): The filename / path
        search_string (str): The string after which to insert the line of text
        new_string (str): The string to be inserted
    """
    if not new_string or not search_string:
        return
    text = ""
    with open(filename, mode="r", encoding="utf-8") as a_file:
        # read line by line instead of reading the entire file at once
        for line in a_file:
            text += line
        text = text.splitlines(True)
        line_number = 0
        insert_str_at_line_nr = []
        for line in text:
            if search_string in line:
                insert_str_at_line_nr.append(line_number + 1)
            line_number += 1
        for i in reversed(insert_str_at_line_nr):
            # insert from the end so that the you don't affect the index number
            # as you insert (the list is growing)
            text.insert(i, new_string)
    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.writelines(text)
