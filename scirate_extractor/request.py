import requests


from .parser import ScirateParser


class ScirateRequestException(Exception):
    """ """ 
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.url, ':', self.error_msg


class ScirateRequest():
    """ """
    def __init__(self, client, path, query_dict, req_format):
        """Initialize request object."""
        self.params = query_dict
        self.host = client.base_url
        self.path = path
        self.req_format = req_format

        self.parser = ScirateParser()

        for k, v in self.params.items():
            self.path += v

    def request(self):
        resp = requests.get(self.host+self.path)

        if resp.status_code != 200:
            raise ScirateRequestException(resp.reason, self.path)
        if self.req_format == "author":
            return self.parser.parse_author(resp)

        else:
            raise Exception("Invalid format.")
