class CANAnalyzer:

    def __init__(self, bus):
        self.bus = bus

    def capture(self):
        return self.bus.receive_all()
