import cv2

def draw_line(frame, y):
    h, w = frame.shape[:2]
    cv2.line(frame,(0,y),(w,y),(0,0,255),2)

def draw_counts(frame, counts):
    y = 30
    for k,v in counts.items():
        cv2.putText(frame,f"{k}: {v}",
                    (20,y),
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
        y += 30
