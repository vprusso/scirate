"""Scirate author class."""


class ScirateAuthor:
    """Scirate author information."""
    def __init__(self, author_dict, client):
        self._author_dict = author_dict
        self._client = client

    def __repr__(self):
        return self.name

    @property
    def gid(self):
        """Scirate id of author."""
        return self._author_dict["id"]

    @property
    def name(self):
        """Author name."""
        return self._author_dict["name"]

    @property
    def category(self):
        """Author publishing category."""
        return self._author_dict["category"]

    @property
    def papers(self):
        """Papers of the author."""
        return self._author_dict["papers"]

    @property
    def arxiv_ids(self):
        """arXiv ids of papers from author."""
        return self._author_dict["arxiv_ids"]

    @property
    def co_authors(self):
        """Co-authors of author for each paper."""
        return self._author_dict["co_authors"]
