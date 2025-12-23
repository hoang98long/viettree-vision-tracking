from ultralytics import YOLO

model = YOLO("yolov11n.pt")

model.export(
    format="engine",
    device=0,
    half=True,      # FP16
    imgsz=640
)
