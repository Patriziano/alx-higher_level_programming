#!/usr/bin/python3
"""A class that inherits from another"""


class MyList(list):
    """
    A class that inherits from my list

    Args:
        list (int) : the inherited class
        Return:
            Nothing
    """
    def print_sorted(self):
        """
        Prints the sorted output
        """
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=' ')
        print()  # Print a newline at the end
