#!/usr/bin/python3
"""function on text indentation"""


def text_indentation(text):
    """
    Prints a text with two new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.
    Raises:
    TypeError: if text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
