import matplotlib.pyplot as plt

file_name = "logs/data.log"

time = []

velx = []
vely = []
velz = []

accelx = []
accely = []
accelz = []

r = []
p = []
y = []

barometer = []

battery = []

with open(file_name, "r") as file:
    data = file.readlines()

for line in data:
    line = line.strip().split(';')

    T, B, V, A, O, Alt = line

    time.append(float(T.split(':')[1]))
    battery.append(float(B.split(':')[1]))
    barometer.append(float(Alt.split(':')[1]))

    _, vel = V.split(":")
    vel = vel.split(",")

    _, accel = A.split(":")
    accel = accel.split(",")

    _, orient = O.split(":")
    orient = orient.split(",")

    velx.append(float(vel[0]))
    vely.append(float(vel[1]))
    velz.append(float(vel[2]))

    accelx.append(float(accel[0]))
    accely.append(float(accel[1]))
    accelz.append(float(accel[2]))

    r.append(float(orient[0]))
    p.append(float(orient[1]))
    y.append(float(orient[2]))

    
plt.plot(time, velx, color="red", label="X-Velocity")
plt.plot(time, vely, color="green", label="Y-Velocity")
plt.plot(time, velz, color="blue", label="Z-Velocity")

plt.title("Velocity")
plt.legend()
plt.savefig("logs/plots/Velocity.png")
plt.clf()

plt.plot(time, accelx, color="red", label="X-Acceleration")
plt.plot(time, accely, color="green", label="Y-Acceleration")
plt.plot(time, accelz, color="blue", label="Z-Acceleration")

plt.title("Acceleration")
plt.legend()
plt.savefig("logs/plots/Acceleration.png")
plt.clf()

plt.plot(time, r, color="red", label="Rolll")
plt.plot(time, p, color="green", label="Pitch")
plt.plot(time, y, color="blue", label="Yaw")

plt.title("Orientation")
plt.legend()
plt.savefig("logs/plots/Orientation.png")
plt.clf()

plt.plot(time, battery, color="black", label="Battery")

plt.title("Battery")
plt.legend()
plt.savefig("logs/plots/Battery.png")
plt.clf()

plt.plot(time, barometer, color="black", label="Barometer")
plt.title("Barometer")
plt.legend()
plt.savefig("logs/plots/Barometer.png")
