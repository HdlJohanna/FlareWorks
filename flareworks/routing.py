import typing


class HTTPMap:
    def __init__(self,rules):
        self.rules = rules

    def get_rule(self,endpoint) -> typing.Optional["Rule"]:
        for rule in self.rules:
            if rule.endpoint == endpoint:
                return rule

        return None

    def add_rule(self,rule):
        self.rules.append(rule)

class Rule:
    def __init__(self,endpoint,flare_master,function,methods=["GET"]):
        self.endpoint = endpoint
        self.master = flare_master
        self.function = function
        self.methods = methods