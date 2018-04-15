import datetime


from .author import ScirateAuthor
from .category import ScirateCategory
from .paper import SciratePaper
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

    def author(self, first_name, last_name, category):
        """Get info about an author."""
        author_id = last_name + "_" + first_name[0] + "+in:" + category
        params = {"id": author_id, 
                  "first_name": first_name,
                  "last_name": last_name,
                  "category": category}

        resp = self.request("/search?q=au:", params, req_format="author")
        return ScirateAuthor(resp["author"], self)

    def paper(self, arxiv_id):
        """Get info about a paper."""
        params = {"id": arxiv_id}

        resp = self.request("/arxiv/", params, req_format="paper")
        return SciratePaper(resp["paper"], self)

    def category(self, category, date=datetime.datetime.today().strftime('%Y-%m-%d')):
        """Get arxiv listings for category."""
        search_id = category + "?date=" + date
        params = {"id": search_id,
                  "category": category,
                  "date": date}

        resp = self.request("/arxiv/", params, req_format="category")
        return ScirateCategory(resp["category"], self)
