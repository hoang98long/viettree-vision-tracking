import cv2
from utils.config import load_yaml
from utils.logger import get_logger
from utils.fps import FPS

from vision.camera.usb_camera import USBCamera
from vision.camera.video_file import VideoFileCamera
from models.yolov11.infer import YOLOv11Infer
from models.trackers.simple_tracker import SimpleTracker
from logic.counter.line_counter import LineCounter
from logic.state.system_state import SystemState
from logic.state.camera_state import CameraState
from services.exporter.rest_exporter import RestExporter
import time

class InferPipeline:
    def __init__(self, system_cfg, camera_cfg, model_cfg, counter_cfg):
        self.system = load_yaml(system_cfg)
        self.camera_cfg = load_yaml(camera_cfg)
        self.model_cfg = load_yaml(model_cfg)
        self.counter_cfg = load_yaml(counter_cfg)

        self.logger = get_logger("InferPipeline")

        # Camera
        if self.camera_cfg["type"] == "usb":
            self.camera = USBCamera(self.camera_cfg)
        else:
            self.camera = VideoFileCamera(self.camera_cfg)

        # AI
        self.detector = YOLOv11Infer(
            self.model_cfg["model_path"],
            self.model_cfg["conf_threshold"]
        )

        self.tracker = SimpleTracker()
        self.counter = LineCounter(self.counter_cfg)
        self.fps = FPS()
        self.exporter = RestExporter(
            endpoint=self.system["api_endpoint"],
            device_id=self.system["device_id"]
        )
        self.last_push = time.time()
        self.system_state = SystemState()
        self.camera_state = CameraState()

    def run(self):
        self.logger.info("Infer pipeline started")
        cap = self.camera.open()

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            self.camera_state.update(ret)
            self.system_state.tick()

            detections = self.detector.detect(
                frame,
                self.counter_cfg["classes"]
            )

            tracks = self.tracker.update(detections)
            self.counter.update(tracks)

            self._draw(frame, tracks)
            self.fps.update()

            if self.system.get("show_window", True):
                cv2.imshow("Vision Infer", frame)
                if cv2.waitKey(1) == 27:
                    break

            if time.time() - self.last_push > 10:
                self.exporter.send(self.counter.counts)
                self.last_push = time.time()

        self.camera.release()
        cv2.destroyAllWindows()
        self.logger.info("Infer pipeline stopped")

    def _draw(self, frame, tracks):
        h, w = frame.shape[:2]
        cv2.line(frame, (0,self.counter.line_y),
                 (w,self.counter.line_y),(0,0,255),2)

        for t in tracks:
            x1,y1,x2,y2 = map(int, t.bbox)
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,f"{t.cls}-{t.id}",
                        (x1,y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)

        y = 30
        for k,v in self.counter.counts.items():
            cv2.putText(frame,f"{k}: {v}",
                        (20,y),
                        cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
            y += 30
