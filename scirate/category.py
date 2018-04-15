"""Scirate category class."""


class ScirateCategory:
    """Scirate category information."""
    def __init__(self, category_dict, client):
        self._category_dict = category_dict
        self._client = client

    def __repr__(self):
        return self.category

    @property
    def gid(self):
        """Scirate id of category query."""
        return self._category_dict["id"]

    @property
    def category(self):
        """Publishing category."""
        return self._category_dict["category"]

    @property
    def papers(self):
        """Papers of category."""
        return self._category_dict["papers"]

    @property
    def date(self):
        """Date of papers in category."""
        return self._category_dict["date"]

    @property
    def arxiv_ids(self):
        """arXiv ids of papers in category."""
        return self._category_dict["arxiv_ids"]

    @property
    def co_authors(self):
        """Co-authors for each paper in category."""
        return self._category_dict["co_authors"]

    @property
    def scites(self):
        """Number of scites for each paper in category."""
        return self._category_dict["scites"]
