class ZoneCounter:
    def __init__(self, zones, classes):
        """
        zones = {
          "zoneA": (x1,y1,x2,y2)
        }
        """
        self.zones = zones
        self.reverse = {v:k for k,v in classes.items()}
        self.counts = {k:0 for k in classes}
        self.visited = set()

    def _inside(self, cx, cy, zone):
        x1,y1,x2,y2 = zone
        return x1 <= cx <= x2 and y1 <= cy <= y2

    def update(self, tracks):
        for t in tracks:
            cx, cy = t.history[-1]
            for name, zone in self.zones.items():
                if self._inside(cx, cy, zone):
                    key = (t.id, name)
                    if key not in self.visited:
                        self.counts[t.cls] += 1
                        self.visited.add(key)
    