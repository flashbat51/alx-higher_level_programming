#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    A function that replace all occurrence
    of an element by another in new list,
    by Jnr
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
