class RuleValidator:
    def __init__(self, rules):
        self.rules = rules

    def validate(self, **kwargs):
        for rule in self.rules:
            if not rule.check(**kwargs):
                return False
        return True
