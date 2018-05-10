"""
@author: frndlytm
@name: navigator.paginator
@description:
    An object to maintain the current page of results using
    API limits and offsets.
"""

class Paginator:
    #
    # A Paginator for the Cloudera Navigator API has a limit and an offset.
    # Since queries to the API appear to limit to 100 results by default,
    # we want to pass the parameters to the API by default and use an iterator
    # to access multiple pages.
    #
    def __init__(self, limit=100, offset=0):
        self._limit = limit
        self._offset = offset
        self._finished = False

    #
    # Prints the parameter string the API expects for limit and offset.
    #
    def __str__(self):
        return '&limit={0}&offset={1}'.format(self.limit, self.offset)

    #
    # Make it an iterator by default, relying on finish as a setter
    # for public use.
    #
    def __next__(self):
        if not self.finished:
            self.offset += self.limit
        else:
            raise StopIteration

    def finish(self):
        self.finished = True


    #
    # Follows a strict pattern for setters in case I choose to inherit a
    # Paginator interface.
    #
    @property
    def limit(self):
        return self._limit
    @limit.setter
    def limit(self, limit):
        self._limit = limit

    @property
    def offset(self):
        return self._offset
    @offset.setter
    def offset(self, offset):
        self._offset = offset

    @property
    def finished(self):
        return self._finished
    @finished.setter
    def finished(self, val):
        self._finished = val
