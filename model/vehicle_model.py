import random
import time

class VehicleModel:

    def __init__(self):
        self.speed = 0
        self.rpm = 800
        self.voltage = 12.6
        self.temperature = 25
        self.throttle = 0.1

    def update(self):

        phase = int(time.time()) % 20

        if phase < 5:
            self.throttle = 0.1
        elif phase < 10:
            self.throttle = 0.7
        elif phase < 15:
            self.throttle = 0.3
        else:
            self.throttle = 0.0

        acceleration = self.throttle * 8 - 0.15 * self.speed
        self.speed += acceleration
        self.speed = max(0, min(120, self.speed))

        if self.speed < 20:
            gear_ratio = 60
        elif self.speed < 40:
            gear_ratio = 40
        elif self.speed < 80:
            gear_ratio = 30
        else:
            gear_ratio = 20

        self.rpm = int(800 + self.speed * gear_ratio * (0.6 + self.throttle))

        if random.random() < 0.05:
            self.rpm = int(self.rpm * 0.85)

        self.voltage = 12.5 + random.uniform(-0.1, 0.1)

        # 🌡️ Realistic temperature
        load = self.rpm / 4000

        if self.temperature < 90:
            self.temperature += 0.1 + 0.2 * load
        else:
            self.temperature += random.uniform(-0.05, 0.05)

        if self.speed < 5:
            self.temperature -= 0.05

        if self.temperature > 95:
            self.temperature -= 0.1

        self.temperature = max(25, min(105, self.temperature))
