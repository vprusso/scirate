import re
import requests
from bs4 import BeautifulSoup


from .util import find_substr_btw


class ScirateParserHelper():
    """Helper class for ScirateParser."""
    def __init__(self):
        self.base_url = "https://scirate.com"

    def author_pagination_url(self, page, params):
        """Create Scirate pagination URL."""
        return self.base_url+"/search?page="+str(page)+"&q=au%3A"+params["id"]+"+in%3A"+params["category"]

    def check_no_papers_found(self, url):
        """Returns true if pagination URL has no results."""
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, "lxml")
        paper_html = soup.findAll("div", attrs={"class": "title"})
        return paper_html == []

    def date_to_scirate_date_format(self, day, month, year):
        """Take in a day (integer), month (three-letter month code), and year
        (integer). Convert to Scirate date format YYYY-MM-DD."""
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return year + "-" + str(months.index(month) + 1) + "-" + day


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
        self.parser_helper = ScirateParserHelper()

    def parse_author(self, resp, params):
        """Parse author information from Scirate."""
        soup = BeautifulSoup(resp.content, "lxml")

        name = params["first_name"] + " " + params["last_name"]
        paper_html = soup.findAll("div", attrs={"class": "title"})
        author_html = soup.findAll("div", attrs={"class": "authors"})

        arxiv_ids = []
        papers = []
        co_authors = []

        page_count = 1
        page = self.parser_helper.author_pagination_url(page_count, params)

        while not self.parser_helper.check_no_papers_found(page):

            # Paper Titles and arXiv ids for Author:
            for div in paper_html:
                links = div.findAll("a")
                for a in links:
                    arxiv_id = a["href"].split("/arxiv/")
                    arxiv_ids.append(arxiv_id[1])
                    papers.append(a.contents[0])

            # Co-Authors for each Paper:
            for div in author_html:
                links = div.findAll("a")
                co_author = []
                for a in links:
                    co_author.append(a.contents[0].strip(",").rstrip())
                co_authors.append(co_author)

            page_count += 1
            page = self.parser_helper.author_pagination_url(page_count, params)

            resp = requests.get(page)
            soup = BeautifulSoup(resp.content, "lxml")
            paper_html = soup.findAll("div", attrs={"class": "title"})
            author_html = soup.findAll("div", attrs={"class": "authors"})

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

        # Paper Title:
        title = title_html[0].text

        # Paper Abstract:
        abstract = abstract_html[0].text

        # Paper Scites:
        scites = int(scites_html[0].text)

        date = date_html[0].text
        submitted_date = find_substr_btw(date, "Submitted", "to").rstrip().lstrip()
        published_date = find_substr_btw(date, "Published", "").rstrip().lstrip()

        # Submission Date:
        submitted_date_split = submitted_date.split()
        submitted_day = submitted_date_split[0]
        submitted_month = submitted_date_split[1]
        submitted_year = submitted_date_split[2]
        submitted_date = self.parser_helper.date_to_scirate_date_format(submitted_day, submitted_month, submitted_year)

        # Publication Date:
        published_date_split = published_date.split()
        published_day = published_date_split[0]
        published_month = published_date_split[1]
        published_year = published_date_split[2]
        published_date = self.parser_helper.date_to_scirate_date_format(published_day, published_month, published_year)

        # Author Comments from arXiv:
        author_comments = soup.body.findAll(text=re.compile("Author comments:"))
        author_comments = author_comments[0].split(":")[1].rstrip().lstrip()

        # arXiv Category:
        category = ""
        for div in date_html:
            links = div.findAll("a")
            for a in links:
                category = a.contents[0]

        # Authors on Paper:
        authors = []
        for div in author_html:
            links = div.findAll("a")
            for a in links:
                authors.append(a.contents[0])

        # Scirate Users who Scited Paper:
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

    def parse_category(self, resp, params):
        soup = BeautifulSoup(resp.content, "lxml")

        paper_html = soup.findAll("div", attrs={"class": "title"})
        author_html = soup.findAll("div", attrs={"class": "authors"})
        scites_html = soup.findAll("button", attrs={"class": "btn btn-default count"})

        arxiv_ids = []
        co_authors = []
        papers = []
        scites = []

        # Paper Scites:
        for scite in scites_html:
            scites.append(int(scite.text))

        # Paper Titles and arXiv ids for Author:
        for div in paper_html:
            links = div.findAll("a")
            for a in links:
                arxiv_id = a["href"].split("/arxiv/")
                arxiv_ids.append(arxiv_id[1])
                papers.append(a.contents[0])

        # Co-Authors for each Paper:
        for div in author_html:
            links = div.findAll("a")
            co_author = []
            for a in links:
                co_author.append(a.contents[0].strip(",").rstrip())
            co_authors.append(co_author)

        category_dict = {"id": params["id"],
                         "category": params["category"],
                         "date": params["date"],
                         "papers": papers,
                         "arxiv_ids": arxiv_ids,
                         "co_authors": co_authors,
                         "scites": scites}

        data_dict = {"ScirateResponse": {"category": category_dict}}
        return data_dict["ScirateResponse"]
