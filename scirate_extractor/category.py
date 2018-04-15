"""Scirate category class."""


class ScirateCategory:
    """Scirate category information."""
    def __init__(self, category_dict, client):
        self._category_dict = category_dict
        self._client = client

    def __repr__(self):
        return self.name

    @property
    def gid(self):
        """Scirate id of category query."""
        return self._category_dict["id"]

    @property
    def name(self):
        """Category name."""
        return self._category_dict["name"]

    @property
    def category(self):
        """Publishing category."""
        return self._category_dict["category"]

    @property
    def papers(self):
        """Papers of category."""
        return self._category_dict["papers"]
