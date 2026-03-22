import matplotlib.pyplot as plt

def plot_data(rpm, speed, voltage, temp):

    plt.figure()

    plt.subplot(4,1,1)
    plt.plot(rpm)
    plt.title("RPM")

    plt.subplot(4,1,2)
    plt.plot(speed)
    plt.title("Speed")

    plt.subplot(4,1,3)
    plt.plot(voltage)
    plt.title("Voltage")

    plt.subplot(4,1,4)
    plt.plot(temp)
    plt.title("Temperature")

    plt.tight_layout()
    plt.show()
