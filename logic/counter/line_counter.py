class LineCounter:
    def __init__(self, cfg):
        self.line_y = cfg["line_y"]
        self.class_map = cfg["classes"]
        self.reverse = {v:k for k,v in self.class_map.items()}

        self.counted_ids = set()
        self.counts = {k:0 for k in self.class_map}

    def update(self, tracks):
        for t in tracks:
            if len(t.history) < 2:
                continue

            prev_y = t.history[-2][1]
            curr_y = t.history[-1][1]

            if prev_y < self.line_y <= curr_y:
                key = (t.id, t.cls)
                if key not in self.counted_ids:
                    self.counts[t.cls] += 1
                    self.counted_ids.add(key)
