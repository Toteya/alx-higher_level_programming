#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    done = False
    while (not done):
        try:
            new_list.insert(new_list.index(search), replace)
            new_list.remove(search)
        except ValueError:
            done = True
    return new_list
