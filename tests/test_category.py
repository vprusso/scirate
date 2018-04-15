from scirate.client import ScirateClient


class TestCategory():
    @classmethod
    def setup_class(cls):
        client = ScirateClient()
        cls.category = client.category("quant-ph", "2017-9-7")

    def test_category(self):
        assert self.category.category == "quant-ph"

    def test_arxiv_ids(self):
        assert self.category.arxiv_ids[1] == "1709.01837"

    def test_scites(self):
        assert len(self.category.scites) == 14
        assert self.category.scites[1] == 31

    def test_papers(self):
        assert len(self.category.papers) == 14

    def test_date(self):
        assert self.category.date == "2017-9-7"

    def co_authors(self):
        assert self.category.co_authors[1][0] == "Vincent Russo"
        assert self.category.co_authors[1][1] == "John Watrous"
