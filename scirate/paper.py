""" Scirate paper class."""
from . import author


class SciratePaper:
    """Scirate paper information."""
    def __init__(self, paper_dict, client):
        self._paper_dict = paper_dict
        self._client = client

    def __repr__(self):
        return self.title

    @property
    def arxiv_id(self):
        """Scirate id of paper."""
        return self._paper_dict["id"]

    @property
    def submitted_date(self):
        """Date of paper submission."""
        return self._paper_dict["submitted_date"]

    @property
    def published_date(self):
        """Date of paper publication."""
        return self._paper_dict["published_date"]

    @property
    def author_comments(self):
        """Author comments on paper."""
        return self._paper_dict["author_comments"]

    @property
    def title(self):
        """Title of paper."""
        return self._paper_dict["title"]

    @property
    def abstract(self):
        """Abstract of paper."""
        return self._paper_dict["abstract"]

    @property
    def scites(self):
        """Number of scites on paper."""
        return self._paper_dict["scites"]

    @property
    def scitors(self):
        """Users who scited paper."""
        return self._paper_dict["scitors"]

    @property
    def category(self):
        """Paper publishing category."""
        return self._paper_dict["category"]

    @property
    def authors(self):
        """Authors of paper."""
        return self._paper_dict["authors"]
