import time

class FPS:
    def __init__(self):
        self.start = time.time()
        self.count = 0

    def update(self):
        self.count += 1
        if self.count % 30 == 0:
            fps = self.count / (time.time() - self.start)
            print(f"FPS: {fps:.2f}")
