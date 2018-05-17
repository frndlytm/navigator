"""
@author: frndlytm
@name: navigator.handler
@description:
    A rule handler class for formatting parameterized API queries.
"""
from jinja2 import Template

class RuleHandler:
    def checkParams(self, params):
        raise NotImplementedError

    def handleParams(self, params):
        raise NotImplementedError

class NoneRuleHandler(RuleHandler):
    def checkParams(self, params=None):
        return True
    def handlerParams(self, params=None):
        return ''


class AuditRuleHandler(RuleHandler):
    class AuditRule:
        def __init__(self, start, end, query):
            self.start = start
            self.end = end
            self.query = query

        def __str__(self):
            return 'startTime={}&endTime={}&format=JSON&attachment=false&{}'.format(
                self.start, self.end, self._query()
            )

        def _query(self):
            return '&'.join(['query='+q for q in self.query])

    def checkParams(self, params):
        try:
            keys = params.keys()
            assert 'startTime' in keys
            assert 'endTime' in keys
            assert 'query' in keys
            return True
        except:
            return False


    def handleParams(self, params):
        if self.checkParams(params):
            audit = self.AuditRule(params['startTime'], params['endTime'], params['query'])
            return str(audit)


class InteractiveRuleHandler(RuleHandler):
    class InteractiveRule:
        def __init__(self, query):
            self.query = query
        def __str__(self):
            return ';'.join(
                ['{}:{}'.format(key, value) for key, value in self.query]
            )

    def checkParams(self, params):
        return True

    def handleParams(self, params):
        if self.checkParams(params):
            interactive = self.InteractiveRule(params['query'])
            return 'query={}'.format(str(interactive))