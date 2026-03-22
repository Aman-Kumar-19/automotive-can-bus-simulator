# 🚗 Automotive CAN Bus Simulator & Analyzer

A Python-based simulation of an automotive CAN network that emulates multiple Electronic Control Units (ECUs), transmits CAN frames over a virtual bus, decodes signals, and visualizes vehicle telemetry — all without requiring physical CAN hardware.

---

## 📌 Overview

This project demonstrates core automotive software concepts:

* CAN message structure and communication
* ECU behavior simulation
* Signal encoding & decoding
* Vehicle telemetry analysis

It mimics how real automotive diagnostic tools (like CAN analyzers) work.

---

## 🏗️ System Architecture

```
ECU Simulator
     ↓
Virtual CAN Bus
     ↓
CAN Analyzer
     ↓
Signal Decoder
     ↓
Telemetry Visualization
```

---

## 🧩 Components

### 1️⃣ ECU Simulator

Simulates real vehicle ECUs:

* Engine ECU → RPM
* Speed ECU → Vehicle speed
* Battery ECU → Voltage
* Temperature ECU → Coolant temperature

Each ECU sends CAN frames at different intervals.

---

### 2️⃣ Virtual CAN Bus

A software-based message queue that mimics CAN communication.

* Supports multiple ECUs
* Thread-safe message handling

---

### 3️⃣ CAN Analyzer

Captures messages from the bus and forwards them for decoding.

---

### 4️⃣ Signal Decoder

Decodes raw CAN data into meaningful signals.

Example:

```
ID: 0x100 → RPM
ID: 0x102 → Speed
```

---

### 5️⃣ Visualization

Plots vehicle telemetry:

* Engine RPM
* Vehicle Speed
* Battery Voltage
* Coolant Temperature

---

## 🚀 Features

* ✅ Multi-ECU simulation using threads
* ✅ Virtual CAN communication (no hardware needed)
* ✅ Realistic vehicle behavior (acceleration, braking, idle)
* ✅ Gear shift simulation
* ✅ Engine temperature modeling (warm-up + stabilization)
* ✅ CAN frame decoding
* ✅ Telemetry visualization using Matplotlib

---

## 📊 Example CAN Frame

```json
{
  "id": "0x100",
  "data": [8, 252],
  "timestamp": 1712345678
}
```

---

## 📂 Project Structure

```
automotive-can-simulator/
│
├── ecu_simulator/
├── can_bus/
├── analyzer/
├── decoder/
├── model/
├── visualization/
│
├── notebooks/
├── can_frame.py
├── main.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/automotive-can-simulator.git
cd automotive-can-simulator
```

Install dependencies:

```bash
pip install matplotlib
```

---

## ▶️ Usage

Run the simulation:

```bash
python main.py
```

Or use the notebook:

```bash
notebooks/demo.ipynb
```

---

## 📈 Output

The simulation generates:

* Real-time CAN messages
* Decoded signal logs
* Telemetry plots

---

## 🎯 Learning Outcomes

This project helps you understand:

* CAN protocol basics
* Automotive system architecture
* ECU communication patterns
* Signal processing & visualization
* Multithreading in Python

---

## 🔮 Future Improvements

* 🔹 DBC file support (industry standard decoding)
* 🔹 Real-time dashboard (GUI)
* 🔹 CAN log replay (.asc / .log)
* 🔹 Fault injection (sensor failures)
* 🔹 J1939 protocol support

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Improve simulation realism
* Add new ECUs
* Enhance visualization
* Implement new protocols

---

## 📄 License

This project is open-source and available under the MIT License.

---

## ⭐ Why This Project?

This repository demonstrates **automotive software engineering concepts without hardware**, making it ideal for:

* Students learning automotive systems
* Engineers exploring CAN communication
* Portfolio projects for embedded/automotive roles

---

## 🙌 Acknowledgment

Inspired by real-world automotive diagnostic tools and CAN analysis workflows.

---

⭐ If you found this project useful, consider giving it a star!
