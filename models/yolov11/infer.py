from ultralytics import YOLO

class YOLOv11Infer:
    def __init__(self, model_path, conf):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame, class_map):
        result = self.model(frame, conf=self.conf, verbose=False)[0]

        detections = []
        for box, cls_id in zip(result.boxes.xyxy, result.boxes.cls):
            cls_id = int(cls_id)
            if cls_id in class_map.values():
                detections.append({
                    "bbox": box.cpu().numpy(),
                    "cls_name": [k for k,v in class_map.items() if v == cls_id][0]
                })
        return detections
