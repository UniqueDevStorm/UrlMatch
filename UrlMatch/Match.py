import re

class Match:
    def __init__(self, query: str):
        self.query = query

    def UrlMatch(self):
        urlmatch = re.compile('https?://(\w*:\w*@)?[-\w.]+(:\d+)?(/([\w/_.]*(\?\S+)?)?)?')
        result = urlmatch.match(self.query)
        if result is None:
            return False
        return True

    def EmailMatch(self):
        emailmatch = re.compile('[0-9a-zA-Z]+@[0-9a-zA-Z]+.[0-9a-zA-Z]+')
        result = emailmatch.match(self.query)
        if result is None:
            return False
        return True