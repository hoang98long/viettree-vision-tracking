class SizeFilterRule:
    def __init__(self, min_area=500, max_area=500000):
        self.min_area = min_area
        self.max_area = max_area

    def check(self, bbox):
        x1,y1,x2,y2 = bbox
        area = (x2-x1)*(y2-y1)
        return self.min_area <= area <= self.max_area
