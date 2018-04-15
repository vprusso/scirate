import re
from bs4 import BeautifulSoup


from .util import find_substr_btw 


class ScirateParserException(Exception):
    """Exception class for ScirateParser."""
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class ScirateParser():
    """Parser for Scirate class."""
    def __init__(self):
        """ """
        pass

    def parse_author(self, resp, params):
        """Parse author information from Scirate."""
        soup = BeautifulSoup(resp.content, "lxml")

        name = params["first_name"] + " " + params["last_name"]
        title_html = soup.findAll("div", attrs={"class": "title"})
        author_html = soup.findAll("div", attrs={"class": "authors"})

        arxiv_ids = []
        papers = []
        for div in title_html:
            links = div.findAll("a")
            for a in links:
                arxiv_ids.append(a["href"])
                papers.append(a.contents[0])

        co_authors = []
        for div in author_html:
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

        title_html = soup.findAll("h1", attrs={"class": "title"})
        abstract_html = soup.findAll("div", attrs={"class": "abstract"})
        scites_html = soup.findAll("button", attrs={"class": "btn btn-default count"})
        scitors_html = soup.findAll("div", attrs={"class": "scites"})
        author_html = soup.findAll("ul", attrs={"class": "authors"})
        date_html = soup.findAll("div", attrs={"class": "dates"})

        title = title_html[0].text
        abstract = abstract_html[0].text
        scites = scites_html[0].text

        date = date_html[0].text
        submitted_date = find_substr_btw(date, "Submitted", "to")
        published_date = find_substr_btw(date, "Published", "")

        author_comments = soup.body.findAll(text=re.compile("Author comments:"))
        author_comments = author_comments[0].split(":")[1]

        category = ""
        for div in date_html:
            links = div.findAll("a")
            for a in links:
                category = a.contents[0]

        authors = []
        for div in author_html:
            links = div.findAll("a")
            author = []
            for a in links:
                author.append(a.contents[0])
            authors.append(author)

        scitors = []
        for div in scitors_html:
            links = div.findAll("a")
            for a in links:
                scitors.append(a.contents[0])

        paper_dict = {"id": params["id"],
                      "title": title,
                      "abstract": abstract,
                      "category": category,
                      "submitted_date": submitted_date,
                      "published_date": published_date,
                      "scites": scites,
                      "scitors": scitors,
                      "author_comments": author_comments,
                      "authors": authors}

        data_dict = {"ScirateResponse": {"paper": paper_dict}}
        return data_dict["ScirateResponse"]


