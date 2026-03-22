import threading
import time
from can_frame import create_frame

class BatteryECU(threading.Thread):

    def __init__(self, bus, vehicle):
        super().__init__()
        self.bus = bus
        self.vehicle = vehicle
        self.running = True

    def run(self):
        while self.running:
            v = int(self.vehicle.voltage * 100)
            data = [v >> 8, v & 0xFF]
            self.bus.send(create_frame(0x101, data))
            time.sleep(0.5)

    def stop(self):
        self.running = False
