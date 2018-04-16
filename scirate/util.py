"""General purpose utility functions."""
import re


def find_substr_btw(input_str, start, end):
    """Find substring in string s between start and end."""
    return re.search("%s(.*)%s" % (start, end), input_str).group(1)
