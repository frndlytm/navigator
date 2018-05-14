"""
@author: frndlytm
@name: navigator.manager
@description:
    A manager consumes all of the factories and builds their results on concrete metadata.
"""
from paginator import Paginator

class Manager:
    def __init__(self):
        self.sources = []
        self.setup()

    @property
    def session(self):
        return self._session
    @session.setter
    def session(self, s):
        self._session = s

    @property
    def factory(self):
        return self._factory
    @factory.setter
    def factory(self, f):
        self._factory = f

    @property
    def meta(self):
        return self._meta
    @meta.setter
    def meta(self, m):
        assert isinstance(m, tuple)
        assert len(m) == 2
        self._meta = m

    @property
    def paginator(self):
        return self._paginator
    @paginator.setter
    def paginator(self, p):
        assert isinstance(p, Paginator)
        self._paginator = p



    def setup(self):
        # Add the source for endpoint lookup.
        src = self.factory.make(None, self.meta[0])
        self.add_source(src)

        # For endpoint in the endpoint lookup, add the source.
        for record in self.sources[0].get(s=self.session)[self.meta[1]]:
            path = record['path'][1:].split('/')
            version = path[0]
            endpoint = path[1]
            src = self.factory.make(version, endpoint)
            self.add_source(src)


    def add_source(self, src):
        self.sources.append(src)


