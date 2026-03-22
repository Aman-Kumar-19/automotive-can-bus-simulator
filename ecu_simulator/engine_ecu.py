import threading
import time
from can_frame import create_frame

class EngineECU(threading.Thread):

    def __init__(self, bus, vehicle):
        super().__init__()
        self.bus = bus
        self.vehicle = vehicle
        self.running = True

    def run(self):
        while self.running:
            rpm = int(self.vehicle.rpm)
            data = [rpm >> 8, rpm & 0xFF]
            self.bus.send(create_frame(0x100, data))
            time.sleep(0.1)

    def stop(self):
        self.running = False
