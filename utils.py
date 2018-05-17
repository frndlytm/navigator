"""
@author: frndlytm
@name: navigator.utils
@description:
    Functions using the core classes to be used in scripting.
"""

def generateUrls(source, query, paginator, breakpoint):
    #
    # Given a source and a query, generate URLs by
    # iterating the paginator up to a breakpoint.
    #
    while paginator.offset < breakpoint:
        url = str(source)+source._query(query)+str(paginator)
        next(paginator)
        yield url