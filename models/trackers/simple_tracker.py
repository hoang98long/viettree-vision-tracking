import math
from collections import deque

class Track:
    def __init__(self, tid, bbox, cls):
        self.id = tid
        self.cls = cls
        self.bbox = bbox
        self.history = deque(maxlen=20)

class SimpleTracker:
    def __init__(self, dist_thresh=50):
        self.dist_thresh = dist_thresh
        self.tracks = {}
        self.next_id = 0

    def _center(self, box):
        x1,y1,x2,y2 = box
        return int((x1+x2)/2), int((y1+y2)/2)

    def update(self, detections):
        updated = []

        for det in detections:
            box = det["bbox"]
            cls = det["cls_name"]
            cx, cy = self._center(box)

            matched = False
            for t in self.tracks.values():
                px, py = t.history[-1]
                if math.hypot(cx-px, cy-py) < self.dist_thresh:
                    t.bbox = box
                    t.history.append((cx,cy))
                    updated.append(t)
                    matched = True
                    break

            if not matched:
                t = Track(self.next_id, box, cls)
                t.history.append((cx,cy))
                self.tracks[self.next_id] = t
                updated.append(t)
                self.next_id += 1

        return updated
