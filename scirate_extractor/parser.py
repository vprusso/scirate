from bs4 import BeautifulSoup


class ScirateParserException(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class ScirateParser():
    def __init__(self):
        """ """
        pass

    def parse_author(self, resp):
        soup = BeautifulSoup(resp.content, 'lxml')

        data = soup.findAll('div', attrs={'class' : 'title'})
        for div in data:
            links = div.findAll('a')
            for a in links:
                print(a['href'])
                print(a.contents[0])

        data_dict = {"ScirateResponse": {"author" : {"name" : "TEST2", "id": "TEST3", "category": "TEST4"} } }
        return data_dict["ScirateResponse"]
