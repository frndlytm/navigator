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

    def make(self, version, endpoint):
        return Source(self.clustername, self.host, self.port, version, endpoint)



class Source:
    def __init__(self, clustername, host, port, version, endpoint):
        self.clustername = clustername
        self.host = host
        self.port = port
        self.version = version
        self.endpoint = endpoint

    def __repr__(self):
        if self.version:
            return 'https://{}.{}:{}/api/{}/{}'.format(
                self.clustername, self.host, self.port, self.version, self.endpoint
            )
        else:
            return 'https://{}.{}:{}/api/{}'.format(
                self.clustername, self.host, self.port, self.endpoint
            )

    def get(self, s=None, params=None):
        if s:
            return s.get(self, params=params).json()
        else:
            return requests.get(self, params=params).json()

