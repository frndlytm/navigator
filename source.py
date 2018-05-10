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


class Source:
    def __init__(self, clustername, sourceurl, port, version, endpoint):
        assert endpoint in ['entities', 'relations', 'sources']
        self.clustername = clustername
        self.sourceurl = sourceurl
        self.port = port
        self.version = version
        self.endpoint = endpoint

    def __repr__(self):
        return 'https://{}.{}:{}/api/v{}/{}'.format(
            self.clustername, self.sourceurl, self.port, self.version, self.endpoint
        )

    def get(self, params):
        return requests.get(self, params).json()

