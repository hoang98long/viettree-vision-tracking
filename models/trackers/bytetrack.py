from .base_tracker import BaseTracker

class ByteTrack(BaseTracker):
    def __init__(self, cfg=None):
        self.cfg = cfg

    def update(self, detections):
        """
        TODO:
        - tích hợp ByteTrack thật
        - output Track(id, bbox, cls)
        """
        raise NotImplementedError("ByteTrack not implemented yet")
