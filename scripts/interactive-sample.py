import sys
import os

sys.path.append('~/path/to/projects/')
path = '~/path/to/data'


def generateUrls(source, query, paginator, breakpoint):
    #
    # Given a source and a query, generate URLs by
    # iterating the paginator up to a breakpoint.
    #
    while paginator.offset < breakpoint:
        url = str(source)+source._query(query)+str(paginator)
        next(paginator)
        yield url


def counter(name, text, current):
    if name in text: current += 1
    return current



if __name__ == '__main__':
    from navigator.settings import config
    from navigator.paginator import Paginator
    from navigator.source import Source
    from navigator.handler import InteractiveRuleHandler

    from datetime import datetime as dt
    import pandas as pd

    #
    # I.
    # Set up the list of queries as a generator.
    #
    session = config.session

    # query rule sent to handler.
    rule = {'query': [('sourceType', 'impala')]}

    # source url wrapper object.
    s = Source(
        'clustername',
        'clusterhost',
        8888, 'v12',
        'interactive/entities?',
        InteractiveRuleHandler()
    )

    # break at totalMatched records to the query, and partition appropriately.
    breakpoint = s.get(config.session, rule)['totalMatched']

    # new Paginator and generate paginated URLs
    p = Paginator(1000, 0)
    g = generateUrls(s, rule, p, breakpoint)



    #
    # II.
    # Count off using the CSV
    #
    data = pd.read_csv(path + 'tables.csv', header=0)
    for url in g:
        # send the request
        resp = session.get(url)

        # print message format:
        # '{timestamp} 200 entites?query=sourceType:impala&limit={}&offset={}'
        print(dt.now(), resp.status_code, url.split('/')[-1])

        # get the text and count occurences
        body = resp.text
        data['resource_cnt'] = data.apply(
            lambda row: counter(row['resource'], body, row['resource_cnt']),
            axis=1
        )
        data['fullname_cnt'] = data.apply(
            lambda row: counter(row['fullname'], body, row['fullname_cnt']),
            axis=1
        )
        data['database_cnt'] = data.apply(
            lambda row: counter(row['database'], body, row['database_cnt']),
            axis=1
        )
        data['tablename_cnt'] = data.apply(
            lambda row: counter(row['tablename'], body, row['tablename_cnt']),
            axis=1
        )

    #
    # III.
    # Send the data to file
    #
    data.to_csv(path+'results.csv')


