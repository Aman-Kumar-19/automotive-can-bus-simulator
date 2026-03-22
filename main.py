import time

from can_bus.message_bus import VirtualCANBus
from analyzer.capture import CANAnalyzer
from decoder.signal_decoder import SignalDecoder
from model.vehicle_model import VehicleModel

from ecu_simulator.engine_ecu import EngineECU
from ecu_simulator.speed_ecu import SpeedECU
from ecu_simulator.battery_ecu import BatteryECU
from ecu_simulator.temperature_ecu import TemperatureECU

from visualization.telemetry_plot import plot_data


def main():

    bus = VirtualCANBus()
    vehicle = VehicleModel()

    engine = EngineECU(bus, vehicle)
    speed = SpeedECU(bus, vehicle)
    battery = BatteryECU(bus, vehicle)
    temp = TemperatureECU(bus, vehicle)

    engine.start()
    speed.start()
    battery.start()
    temp.start()

    analyzer = CANAnalyzer(bus)
    decoder = SignalDecoder()

    rpm_data, speed_data, voltage_data, temp_data = [], [], [], []

    for _ in range(200):

        vehicle.update()
        frames = analyzer.capture()

        for frame in frames:
            signal, value = decoder.decode(frame)

            if signal == "RPM":
                rpm_data.append(value)
            elif signal == "Speed":
                speed_data.append(value)
            elif signal == "Voltage":
                voltage_data.append(value)
            elif signal == "Temp":
                temp_data.append(value)

        time.sleep(0.1)

    engine.stop()
    speed.stop()
    battery.stop()
    temp.stop()

    plot_data(rpm_data, speed_data, voltage_data, temp_data)


if __name__ == "__main__":
    main()
