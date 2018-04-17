import datetime


from scirate.client import ScirateClient


class TestCategory():
    @classmethod
    def setup_class(cls):
        client = ScirateClient()
        cls.category = client.category("quant-ph", "2017-9-7")
        cls.category_no_date = client.category("quant-ph")

    def test_category(self):
        today_date = datetime.datetime.today().strftime('%Y-%m-%d')

        assert len("quant-ph") == len(self.category.category)
        assert len("quant-ph") == len(self.category_no_date.category)

        assert self.category.gid == "quant-ph?date=2017-9-7"
        assert self.category_no_date.gid == "quant-ph?date="+str(today_date)

        assert repr(self.category) == "quant-ph"
        assert self.category.category == "quant-ph"

        assert repr(self.category_no_date) == "quant-ph"
        assert self.category_no_date.category == "quant-ph"

    def test_arxiv_ids(self):
        assert self.category.arxiv_ids[1] == "1709.01837"

    def test_scites(self):
        assert len(self.category.scites) == 15
        assert self.category.scites[1] == 31

    def test_papers(self):
        assert len(self.category.papers) == 15
        assert self.category.papers[-1] == "Modeling Quantum Behavior in the Framework of Permutation Groups"

    def test_date(self):
        assert self.category.date == "2017-9-7"

    def co_authors(self):
        assert len(self.category.co_authors) == 2
        assert self.category.co_authors[1][0] == "Vincent Russo"
        assert self.category.co_authors[1][1] == "John Watrous"
