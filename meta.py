"""
@author: frndlytm
@name: navigator.meta
@description:
    Houses all the various look-up information and 'config' classes.
"""
from enum import Enum

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
