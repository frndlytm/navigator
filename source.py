"""
@author: cdimare@granitenet.com
@name: navigator.source
@description:
    Exposes the cluster by managing metadata and generating requests.
"""
import requests

class SourceFactory:
    def __init__(self, clustername, host, port):
        self.clustername = clustername
        self.host = host
        self.port = port

    def make(self, version, endpoint, handler):
        return Source(self.clustername, self.host, self.port, version, endpoint, handler)



class Source:
    def __init__(self, clustername, host, port, version, endpoint, handler):
        self.clustername = clustername
        self.host = host
        self.port = port
        self.version = version
        self.endpoint = endpoint
        self.handler = handler

    def __repr__(self):
        if self.version:
            return 'https://{}.{}:{}/api/{}/{}'.format(
                self.clustername, self.host, self.port, self.version, self.endpoint
            )
        else:
            return 'https://{}.{}:{}/api/{}'.format(
                self.clustername, self.host, self.port, self.endpoint
            )

    def _query(self, params):
        return self.handler.handleParams(params)

    def get(self, s=None, params=None):
        url = str(self)+self._query(params)
        if s: return s.get(url).json()
        else: return requests.get(url).json()

