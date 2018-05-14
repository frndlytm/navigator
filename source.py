"""
@author: cdimare@granitenet.com
@name: navigator.source
@description:
    Exposes the cluster by managing metadata and generating requests.
"""
import requests
from paginator import DefaultPaginator


class SourceFactory:
    def __init__(self, clustername, host, port):
        self.clustername = clustername
        self.host = host
        self.port = port

    def make(self, endpoint, paginator=DefaultPaginator()):
        return Source(self.clustername, self.host, self.port, endpoint, paginator)



class Source:
    def __init__(self, clustername, host, port, endpoint, paginator):
        self.clustername = clustername
        self.host = host
        self.port = port
        self.endpoint = endpoint
        self.paginator = paginator

    def __repr__(self):
        return 'https://{}.{}:{}/api/{}'.format(
            self.clustername, self.host, self.port, self.endpoint
        )

    def get(self, params):
        return requests.get(self, params).json()

