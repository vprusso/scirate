from scirate_extractor.client import ScirateClient


class TestPaper():
    @classmethod
    def setup_class(cls):
        client = ScirateClient()
        cls.paper = client.paper("1709.01837")

    def test_arxiv_id(self):
        assert self.paper.arxiv_id == "1709.01837"

    def test_submitted_date(self):
        pass

    def test_published_date(self):
        pass

    def test_author_comments(self):
        assert(self.paper.author_comments == "11 pages")

    def test_title(self):
        assert(self.paper.title == "Extended Nonlocal Games from Quantum-Classical Games")

    def test_abstract(self):
        assert(self.paper.abstract[0:44] == "Several variants of nonlocal games have been")

    def test_scites(self):
        assert(self.paper.scites > 30)

    def test_scitors(self):
        assert(self.paper.scites == len(self.paper.scitors))
        assert(self.paper.scitors[0] == "Alessandro")

    def test_category(self):
        assert(self.paper.category == "quant-ph")

    def test_authors(self):
        assert(self.paper.authors[0] == "Vincent Russo")
        assert(self.paper.authors[1] == "John Watrous")

