import requests
import datetime

class RestExporter:
    def __init__(self, endpoint, device_id):
        self.endpoint = endpoint
        self.device_id = device_id

    def send(self, counts):
        payload = {
            "device_id": self.device_id,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "counts": counts
        }
        try:
            requests.post(self.endpoint, json=payload, timeout=3)
        except Exception as e:
            print("Exporter error:", e)
