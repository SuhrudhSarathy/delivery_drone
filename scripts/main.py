from controller import TelloController
from djitellopy import Tello

my_tello = Tello()

points = [[0, 0, 0], [100, 100, 100], [100, 200, 200]]

print(points)

settings = {
    "speed": 0.5,
    "safe_altitude": 0.5
}
controller = TelloController(my_tello)
controller.__init_controller__()
controller.execute_path(points)