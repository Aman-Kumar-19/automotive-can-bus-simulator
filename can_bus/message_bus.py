import threading

class VirtualCANBus:

    def __init__(self):
        self.messages = []
        self.lock = threading.Lock()

    def send(self, frame):
        with self.lock:
            self.messages.append(frame)

    def receive_all(self):
        with self.lock:
            data = self.messages.copy()
            self.messages.clear()
        return data
