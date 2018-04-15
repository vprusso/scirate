"""General purpose utility functions."""
import re


def find_substr_btw(s, start, end):
    """Find substring in string s between start and end."""
    return re.search("%s(.*)%s" % (start, end), s).group(1)
