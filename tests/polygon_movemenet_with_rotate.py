"""The drone has to cover a square, triangle and a pentagon using rotate clockwise. This tests the openloop control of the drone"""
from djitellopy import Tello as Drone
from time import sleep

drone = Drone()

# connect and takeoff
drone.connect()
drone.takeoff()

# Square
drone.move_forward(30)
drone.rotate_clockwise(90)

drone.move_forward(30)
drone.rotate_clockwise(90)

drone.move_forward(30)
drone.rotate_clockwise(90)

drone.move_forward(30)
drone.rotate_clockwise(90)

# Traingle
drone.move_forward(30)
drone.rotate_clockwise(120)

drone.move_forward(30)
drone.rotate_clockwise(120)

drone.move_forward(30)
drone.rotate_clockwise(120)

# Pentagon
drone.move_forward(30)
drone.rotate_clockwise(72)

drone.move_forward(30)
drone.rotate_clockwise(72)

drone.move_forward(30)
drone.rotate_clockwise(72)

drone.move_forward(30)
drone.rotate_clockwise(72)

drone.move_forward(30)
drone.rotate_clockwise(72)

# Land
drone.land()