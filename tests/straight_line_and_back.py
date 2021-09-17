"""This is to test the open loop control of the drone.
We will check if the drone can go front and come back exactly to the same position
"""
from djitellopy import Tello as Drone
from time import sleep

drone = Drone()

drone.connect()
drone.takeoff()

# Move forward and come back

# Move Forward 75 cm
drone.move_forward(75)
sleep(2)

# Move back 75 cm
drone.move_back(75)
sleep(2)

# # Move left and come back
# # Move Left
# drone.move_left(75)
# sleep(2)

# # Move right
# drone.move_right(75)
# sleep(2)

# # Move up 100 cm
# drone.move_up(100)
# sleep(2)

# # Move down 100 cm
# drone.move_down(100)
# sleep(2)

drone.land()



