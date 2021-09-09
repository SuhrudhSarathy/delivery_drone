"""Run the video capture in a separate thread and the movement in a separate thread"""
from djitellopy import Tello as Drone
from threading import Thread
from time import sleep

class MyDrone:
    def __init__(self, data_enabled=True, logfile="data.log"):
        self.data_enabled = data_enabled
        self.drone = Drone()
        self.drone.connect()
        self.logfile = logfile

        if self.data_enabled:
            self.__init__stream__()

        self.drone.takeoff()

    def __init__stream__(self):
        # Initialises stream and shows it in a OpenCV Window
        self.stream_obj = self.drone.get_frame_read()

        self.data_thread = Thread(target=self.show_video)
        self.data_thread.start()

    def log_data(self):
        with open(self.logfile, "a") as file:
            string = f"""Battery: {self.drone.get_battery()}, Velocity: {self.drone.get_speed_x} {self.drone.get_speed_y} {self.drone.get_speed_z}
            Acceleration: {self.drone.get_acceleration_x} {self.drone.get_acceleration_y} {self.drone.get_acceleration_z}, Altitude: {self.drone.get_height}
            ---
            """
            file.write(string)


    def land(self):
        """Shut down all the threads and Land calmly"""

        self.drone.land()
        self.data_thread.join()

        print("Terminated Perfectly")

if __name__ == "__main__":
    drone = MyDrone(True)

    sleep(10)

    drone.land()

    

