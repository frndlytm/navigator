"""
@author: frndlytm
@name: navigator.manager
@description:
    A manager consumes all of the factories and builds their results on concrete metadata.
"""
from paginator import Paginator
import handler

class Manager:
    def __init__(self):
        self.sources = []
        self._session = None
        self._factory = None
        self._paginator = None
        self._docs = None

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
    def docs(self):
        return self._docs
    @docs.setter
    def docs(self, d):
        assert isinstance(d, tuple)
        assert len(d) == 2
        self._docs = d

    @property
    def paginator(self):
        return self._paginator
    @paginator.setter
    def paginator(self, p):
        assert isinstance(p, Paginator)
        self._paginator = p



    def setup(self):
        # Add the source for endpoint lookup.
        src = self.factory.make(None, self.docs[0], handler.NoneRuleHandler())
        self.add_source(src)

        # For endpoint in the endpoint lookup, add the source.
        for record in self.sources[0].get(s=self.session)[self.docs[1]]:
            path = record['path'][1:].split('/')
            version = path[0]
            endpoint = path[1]
            src = self.factory.make(version, endpoint)
            self.add_source(src)


    def add_source(self, src):
        self.sources.append(src)



