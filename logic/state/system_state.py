from logic.state.base_state import BaseState

class SystemState(BaseState):
    def __init__(self):
        self.start_time = None
        self.frame_count = 0
        self.running = False

    def start(self):
        import time
        self.start_time = time.time()
        self.running = True

    def stop(self):
        self.running = False

    def tick(self):
        self.frame_count += 1

    def reset(self):
        self.__init__()
