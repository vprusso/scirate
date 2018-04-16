from scirate.client import ScirateClient


class TestAuthor():
    @classmethod
    def setup_class(cls):
        client = ScirateClient()
        cls.author = client.author("Vincent", "Russo", "quant-ph")

    def test_get_author(self):
        assert self.author.gid == "Russo_V+in:quant-ph"
        assert repr(self.author) == "Vincent Russo"

    def test_author_name(self):
        assert self.author.name == "Vincent Russo"

    def test_author_papers(self):
        papers = self.author.papers
        assert papers[-1] == "Small sets of locally indistinguishable orthogonal maximally entangled states"

    def test_author_category(self):
        assert self.author.category == "quant-ph"

    def test_author_co_authors(self):
        assert self.author.co_authors[-1][0] == "Alessandro Cosentino"
        assert self.author.co_authors[-1][1] == "Vincent Russo"

    def test_author_arxiv_ids(self):
        assert self.author.arxiv_ids[-1] == "1307.3232"
