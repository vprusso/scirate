from bs4 import BeautifulSoup


class ScirateParserException(Exception):
    """ """
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class ScirateParser():
    """ """ 
    def __init__(self):
        """ """
        pass

    def parse_author(self, resp, params):
        """Parse author information from Scirate."""
        soup = BeautifulSoup(resp.content, "lxml")

        name = params["first_name"] + " " + params["last_name"]
        title_divs = soup.findAll("div", attrs={"class": "title"})
        author_divs = soup.findAll("div", attrs={"class": "authors"})

        arxiv_ids = []
        papers = []
        for div in title_divs:
            links = div.findAll("a")
            for a in links:
                arxiv_ids.append(a["href"])
                papers.append(a.contents[0])

        co_authors = []
        for div in author_divs:
            links = div.findAll("a")
            co_author = []
            for a in links:
                co_author.append(a.contents[0])
            co_authors.append(co_author)

        author_dict = {"arxiv_ids": arxiv_ids,
                       "papers": papers,
                       "co_authors": co_authors,
                       "name": name,
                       "id": params["id"],
                       "category": params["category"]}

        data_dict = {"ScirateResponse": {"author": author_dict}}
        return data_dict["ScirateResponse"]

    def parse_paper(self, resp, params):
        """Parse paper information from Scirate."""
        soup = BeautifulSoup(resp.content, "lxml")

        title_div = soup.findAll("h1", attrs={"class": "title"})
        abstract_div = soup.findAll("div", attrs={"class": "abstract"})
        author_divs = soup.findAll("ul", attrs={"class": "authors"})

        title = title_div[0].text

        abstract = abstract_div[0].text

        co_authors = []
        for div in author_divs:
            links = div.findAll("a")
            co_author = []
            for a in links:
                co_author.append(a.contents[0])
            co_authors.append(co_author)

        paper_dict = {"title": title,
                      "abstract": abstract,
                      "co_authors": co_authors}

        data_dict = {"ScirateResponse": {"paper": paper_dict}}
        return data_dict["ScirateResponse"]


