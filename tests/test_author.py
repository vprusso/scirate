from scirate_extractor.client import ScirateClient


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
