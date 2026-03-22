from dataclasses import dataclass
import time

@dataclass
class CANFrame:
    can_id: int
    data: list
    timestamp: float

def create_frame(can_id, data):
    return CANFrame(can_id, data, time.time())
