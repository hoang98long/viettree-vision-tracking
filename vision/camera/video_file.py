import cv2
from vision.camera.base_camera import BaseCamera

class VideoFileCamera(BaseCamera):
    def __init__(self, cfg):
        self.cfg = cfg
        self.cap = None

    def open(self):
        self.cap = cv2.VideoCapture(self.cfg["source"])
        return self.cap

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()
