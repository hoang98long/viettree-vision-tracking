import cv2
from vision.camera.base_camera import BaseCamera

class USBCamera(BaseCamera):
    def __init__(self, cfg):
        self.cfg = cfg
        self.cap = None

    def open(self):
        self.cap = cv2.VideoCapture(int(self.cfg["source"]))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cfg["width"])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cfg["height"])
        return self.cap

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()
