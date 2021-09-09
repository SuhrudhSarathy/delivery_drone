"""This file is to test open loop control. The drone goes should in a square"""
from djitellopy import Tello as Drone
from time import sleep

drone = Drone()
drone.connect()
drone.takeoff()

def move_in_square():
    # Go straight 100cm
    drone.move_forward(100)
    drone.move_left(100)
    drone.move_back(100)
    drone.move_right(100)

for i in range(3):
    move_in_square()
    sleep(5)

drone.land()