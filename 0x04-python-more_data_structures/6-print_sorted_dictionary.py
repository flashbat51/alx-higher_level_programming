#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    function to print a dictionary by ordered keys. By Jnr
    """
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
