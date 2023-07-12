#!/usr/bin/python#
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
        text = a_file.read()
        # text = text.split("\n")
        text = text.splitlines(True)
        line_number = 0
        insert_str_at_line_nr = []
        for line in text:
            if search_string in line:
                insert_str_at_line_nr.append(line_number)
            line_number += 1
        for i in insert_str_at_line_nr:
            text.insert(i, new_string)
    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.writelines(text)
