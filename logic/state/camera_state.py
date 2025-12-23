from logic.state.base_state import BaseState

class CameraState(BaseState):
    def __init__(self):
        self.connected = True
        self.last_frame_time = None

    def update(self, success):
        import time
        self.connected = success
        if success:
            self.last_frame_time = time.time()

    def reset(self):
        self.__init__()
