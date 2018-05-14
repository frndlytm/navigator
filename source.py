"""
@author: cdimare@granitenet.com
@name: navigator.source
@description:
    Exposes the cluster by managing metadata and generating requests.
"""
from enum import Enum
import requests

class SourceType(Enum):
    NONE = 1
    MAPREDUCE = 2
    YARN = 3
    HDFS = 4
    HIVE = 5
    PIG = 6
    IMPALA = 7
    OOZIE = 8
    SDK = 9
    SQOOP = 10
    SPARK = 11
    S3 = 12
    CLUSTER = 13



class SourceFactory:
    def __init__(self, clustername, host, port):
        self.clustername = clustername
        self.host = host
        self.port = port

    def make(self, endpoint):
        return Source(self.clustername, self.host, self.port, endpoint)



class Source:
    def __init__(self, clustername, host, port, endpoint):
        self.clustername = clustername
        self.host = host
        self.port = port
        self.endpoint = endpoint

    def __repr__(self):
        return 'https://{}.{}:{}/api/{}'.format(
            self.clustername, self.host, self.port, self.endpoint
        )

    def get(self, params):
        return requests.get(self, params).json()

