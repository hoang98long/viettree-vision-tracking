from logic.rules.direction import DirectionRule
from logic.rules.debounce import DebounceRule
from logic.rules.filter import SizeFilterRule
from logic.state.counter_state import CounterState

class LineCounter:
    def __init__(self, cfg):
        self.line_y = cfg["line_y"]
        self.classes = cfg["classes"]

        self.state = CounterState()

        self.direction_rule = DirectionRule(cfg.get("direction", "down"))
        self.debounce_rule = DebounceRule(interval=cfg.get("debounce", 1.0))
        self.size_rule = SizeFilterRule()

    def update(self, tracks):
        for t in tracks:
            if len(t.history) < 2:
                continue

            prev_y = t.history[-2][1]
            curr_y = t.history[-1][1]

            # RULES
            if not self.direction_rule.check(prev_y, curr_y):
                continue

            if not self.debounce_rule.check(t.id):
                continue

            if not self.size_rule.check(t.bbox):
                continue

            # LINE CROSS
            if prev_y < self.line_y <= curr_y:
                self.state.register(t.id, t.cls)

    @property
    def counts(self):
        return self.state.total_counts
