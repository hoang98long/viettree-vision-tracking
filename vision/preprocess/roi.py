def crop_roi(frame, roi):
    """
    roi = (x1, y1, x2, y2)
    """
    x1,y1,x2,y2 = roi
    return frame[y1:y2, x1:x2]
