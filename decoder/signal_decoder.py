class SignalDecoder:

    def decode(self, frame):

        if frame.can_id == 0x100:
            rpm = (frame.data[0] << 8) | frame.data[1]
            return ("RPM", rpm)

        elif frame.can_id == 0x101:
            v = (frame.data[0] << 8) | frame.data[1]
            return ("Voltage", v / 100)

        elif frame.can_id == 0x102:
            return ("Speed", frame.data[0])

        elif frame.can_id == 0x103:
            return ("Temp", frame.data[0])

        return ("Unknown", None)
