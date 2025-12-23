from logic.state.base_state import BaseState

class CounterState(BaseState):
    def __init__(self):
        self.total_counts = {}
        self.track_history = set()

    def register(self, track_id, cls):
        key = (track_id, cls)
        if key not in self.track_history:
            self.track_history.add(key)
            self.total_counts[cls] = self.total_counts.get(cls, 0) + 1
            return True
        return False

    def reset(self):
        self.__init__()
