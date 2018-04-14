import requests
import xmltodict
import json


class ScirateRequestException(Exception):
    """ """ 
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.url, ':', self.error_msg


class ScirateRequest():
    """ """
    def __init__(self, client, path, query_dict, req_format='xml'):
        """Initialize request object."""
        self.params = query_dict
        #self.params.update(client.query_dict)
        self.host = client.base_url
        self.path = path
        self.req_format = req_format

        for k, v in self.params.items():
            self.path += v

    def request(self):
        resp = requests.get(self.host+self.path)

        if resp.status_code != 200:
            raise ScirateRequestException(resp.reason, self.path)
        if self.req_format == 'xml':
            #print(resp.content)
            data_dict = {"ScirateResponse": {"name" : {"name" : "TEST"}, "author" : {"author" : "TEST2"} } }

            return data_dict["ScirateResponse"]
            #data_dict = xmltodict.parse(resp.content)
            #return data_dict['ScirateResponse']
        #elif self.req_format == 'json':
        #    return json.loads(resp.content)
        else:
            raise Exception("Invalid format.")
