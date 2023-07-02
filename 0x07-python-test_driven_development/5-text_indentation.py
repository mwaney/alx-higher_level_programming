#!/usr/bin/python3
"""Module for printing a
 text with 2 new lines after each of
 these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints text with indentation
    Args:
        text (str): The text to prints.
    Raises:
        TypeError: If `text` isn't string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for letter in ".?:":
        text = text.replace(letter, letter + "\n\n")
    word_list = [words.strip(" ") for words in text.split("\n")]
    result = "\n".join(word_list)
    print(result, end="")
