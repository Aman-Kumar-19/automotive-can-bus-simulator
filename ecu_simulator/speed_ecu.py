import threading
import time
from can_frame import create_frame

class SpeedECU(threading.Thread):

    def __init__(self, bus, vehicle):
        super().__init__()
        self.bus = bus
        self.vehicle = vehicle
        self.running = True

    def run(self):
        while self.running:
            speed = int(self.vehicle.speed)
            self.bus.send(create_frame(0x102, [speed]))
            time.sleep(0.1)

    def stop(self):
        self.running = False
