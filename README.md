# VietTree Vision Counter

AI system for counting objects using camera on edge devices (Jetson Nano).

## Features
- YOLOv11 + Tracking
- Line / Zone counting
- Edge → Server sync
- Jetson Nano optimized

## Run Edge
```bash
python edge/app.py
```
Run Backend
```bash
uvicorn services.api.app:app --host 0.0.0.0 --port 8000
```

---

## 3.2 SOP TRIỂN KHAI NGOÀI HIỆN TRƯỜNG (CỰC QUAN TRỌNG)

### SOP-01: Chuẩn bị
- Jetson Nano + JetPack 4.6
- Camera cố định
- Internet (nếu sync server)

### SOP-02: Lắp camera
- Góc nhìn **vuông góc**
- Không rung
- Đủ ánh sáng

### SOP-03: Cấu hình
- chỉnh `configs/camera.yaml`
- chỉnh `configs/counter.yaml`

### SOP-04: Test
```bash
python edge/app.py
```
### SOP-04: Chạy 24/7
```bash
python edge/watchdog.py
```
