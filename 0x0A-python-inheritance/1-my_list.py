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
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
