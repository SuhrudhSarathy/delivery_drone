"""Run the video capture in a separate thread and the movement in a separate thread"""
from djitellopy import Tello as Drone
from threading import Thread
from time import sleep, time

class MyDrone:
    def __init__(self, data_enabled=True, logfile="logs/data.log"):
        self.data_enabled = data_enabled
        self.drone = Drone()
        self.drone.connect()
        self.logfile = logfile
        self.log_data_var = True

        if self.data_enabled:
             self.__init__stream__()

        # self.drone.takeoff()

    def __init__stream__(self):
        self.data_thread = Thread(target=self.log_data)
        self.data_thread.start()

    def log_data(self):
        try:
            while self.log_data_var:
                battery = self.drone.get_battery()
                velocity = [self.drone.get_speed_x(), self.drone.get_speed_y(), self.drone.get_speed_z()]
                acceleration = [self.drone.get_acceleration_x(), self.drone.get_acceleration_y(), self.drone.get_acceleration_z()]
                orientation = [self.drone.get_roll(), self.drone.get_pitch(), self.drone.get_yaw()]
                altitude = self.drone.get_barometer()
                with open(self.logfile, "a") as file:
                    string = f"Time:{time()};Battery:{battery};Velocity:{velocity[0]},{velocity[1]},{velocity[2]};Acceleration:{acceleration[0]},{acceleration[1]},{acceleration[2]};Orientation:{orientation[0]},{orientation[1]},{orientation[2]};Altitude:{altitude}\n"
                    file.write(string)
                sleep(0.1)
        except KeyboardInterrupt as e:
            # Stop the thread
            self.land()

    def land(self):
        """Shut down all the threads and Land calmly"""

        # self.drone.land()
        self.log_data_var = False
        self.data_thread.join()

        print("Terminated Perfectly")

if __name__ == "__main__":
    drone = MyDrone(True)
    sleep(10)
    drone.land()

    

