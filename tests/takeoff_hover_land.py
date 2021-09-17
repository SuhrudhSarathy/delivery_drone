"""Test to check Takeoff hover and Land capabilities of the DJI Tello"""
from djitellopy import Tello as Drone
from time import sleep

drone = Drone()

# Connect to the drone
drone.connect()

# take off
drone.takeoff()

# Hover for 15 seconds
sleep(5)

# Land
drone.land()

