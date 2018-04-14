from .author import ScirateAuthor
from .request import ScirateRequest


class ScirateClientException(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class ScirateClient():
    base_url = "https://scirate.com"

    def __init__(self):
        """ """
        self.client_key = "KEY"

    @property
    def query_dict(self):
        return {"key": self.client_key}

    def request(self, *args, **kwargs):
        """Create a ScirateRequest object and make that request."""
        req = ScirateRequest(self, *args, **kwargs)
        return req.request()

    def author(self, author_id):
        """Get info about an author."""
        resp = self.request("/search?q=au:", {'id': author_id})
        print(resp['author'])
        return ScirateAuthor(resp['author'], self)

