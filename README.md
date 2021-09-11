# Delivery Drone (WIP)
This is a technology demonstration for a Indoor Delivery Drone in a Hostel. A DJI Tello is being used as a Test Bed. 
Depends on the [DJITelloPy](https://github.com/damiafuentes/DJITelloPy) Repository.

## Repository Structure
1. ### Tests
- Contains all tests that were performed to test the control, datastreaming capabilities of the Tello
- The tests are as follows
    1. [takeoff_hover_land.py](tests/takeoff_hover_land.py): Performs a takeoff, hovers and then lands
    2. [straight_line_and_back.py](tests/straight_line_and_back.py): The drone takes off, moves forward, comes back the same distance and lands. This helps us verify the drift of the drone in Open loop control. We have found that the drift is gnerally less that 10 cm.
    3. [square_around_without_rotate.py](tests/square_around_without_rotate.py): The drone performs a sqaure without any rotation in place. This is also used to test the drift in the Drone.
    4. [polygon_movement_with_rotate.py](tests/polygon_movemenet_with_rotate.py): The drone performs a square, triangle and pentagon with rotation. The drift here is considerable small.
    5. [drone_data_streaming.py](tests/drone_data_streaming.py): Used to test the data streaming from the drone to a log file.
    6. [drone_video_streaming.py](tests/drone_video_streaming.py): Used to stream video from the drone's camera and display it in an OpenCV Window.
2. ### Scripts
- Contains all the Python Files for Autonomous Flight. Presently only contains the controller.
3. ### Logs
- Contains the log file that can be generated by data logging.
- Contains a Python [script](logs/plot_data.py) that can be used to display data.
- Contains sample plots generated during an autonomous flight.

## Troubleshooting
1. In case of an `invalid imu` error, consider waiting till the next day morning 😜. The error is mostly caused by not enough lighting for the drone to figure out where it is.
