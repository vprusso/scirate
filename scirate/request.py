"""Scirate Requests class."""

import requests


from .parser import ScirateParser


class ScirateRequestException(Exception):
    """ScirateRequest Exception class."""
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.url, ':', self.error_msg


class ScirateRequest():
    """ScirateRequest class."""
    def __init__(self, client, path, query_dict, req_format):
        """Initialize request object."""
        self.params = query_dict
        self.host = client.base_url
        self.path = path
        self.req_format = req_format

        self.parser = ScirateParser()

    def request(self):
        """Make web request to Scirate URL."""
        self.path += self.params["id"]
        resp = requests.get(self.host+self.path)

        if resp.status_code != 200:
            raise ScirateRequestException(resp.reason, self.path)
        elif self.req_format == "author":
            return self.parser.parse_author(resp, self.params)
        elif self.req_format == "paper":
            return self.parser.parse_paper(resp, self.params)
        elif self.req_format == "category":
            return self.parser.parse_category(resp, self.params)

        else:
            raise Exception("Invalid format.")
