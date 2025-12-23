class MultiLineCounter:
    def __init__(self, lines, classes):
        """
        lines = [y1, y2, ...]
        """
        self.lines = lines
        self.classes = classes
        self.reverse = {v:k for k,v in classes.items()}
        self.counts = {k:0 for k in classes}
        self.passed = set()

    def update(self, tracks):
        for t in tracks:
            if len(t.history) < 2:
                continue

            prev_y = t.history[-2][1]
            curr_y = t.history[-1][1]

            for ly in self.lines:
                if prev_y < ly <= curr_y:
                    key = (t.id, ly)
                    if key not in self.passed:
                        self.counts[t.cls] += 1
                        self.passed.add(key)
