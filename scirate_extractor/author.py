class ScirateAuthor:
    def __init__(self, author_dict, client):
        self._author_dict = author_dict
        self._client = client

    def __repr__(self):
        return self.name

    @property
    def gid(self):
        """Scirate ID of author."""
        return self._author_dict['id']

    @property
    def name(self):
        """Author name"""
        print("WEFWE")
        print(self._author_dict)
        return "5"
        return self._author_dict['name']

    @property
    def category(self):
        """Author publishing category"""
        return self._author_dict['category']
