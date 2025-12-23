import time

class DebounceRule:
    def __init__(self, interval=1.0):
        self.interval = interval
        self.last_time = {}

    def check(self, track_id):
        now = time.time()
        last = self.last_time.get(track_id, 0)

        if now - last >= self.interval:
            self.last_time[track_id] = now
            return True
        return False
