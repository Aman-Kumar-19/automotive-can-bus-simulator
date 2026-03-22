import threading
import time
from can_frame import create_frame

class TemperatureECU(threading.Thread):

    def __init__(self, bus, vehicle):
        super().__init__()
        self.bus = bus
        self.vehicle = vehicle
        self.running = True

    def run(self):
        while self.running:
            temp = int(self.vehicle.temperature)
            self.bus.send(create_frame(0x103, [temp]))
            time.sleep(1)

    def stop(self):
        self.running = False
