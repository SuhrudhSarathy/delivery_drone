from threading import Thread
from djitellopy import Tello
from time import sleep

class TelloController:
    def __init__(self, drone: Tello, **kwargs):
        """Main Controller Class
        The main objective of the class is to function as a waypoint to waypoint controller using the Tello's internal
        move commands or the go commands
        Args:
        drone: The initialised Tello instance
        """
        self.drone = drone
        assert self.drone is not None, "Pass a valid Tello Instance"

        # Connect to the Tello and takeoff on initialisation

        self.drone.connect()
        self.speed = kwargs["speed"]
        self.safe_altitude = kwargs["safe_altitude"]
        
        # Data collection from the Drone
        self.velocity = [0, 0, 0]
        self.acceleration = [0, 0, 0]
        self.orientation = [0, 0, 0]
        self.altitude = 0
        self.battery = 0

        self.state = "Armed"

        # Start a thread to update the recent data
        self.data_thread = Thread(target=self.__get_data__())

    def __get_data__(self):
        """Function to get data from the drone. This will run on a different thread.
        All exception handling will happen in a main function where on any Exception this thread will be closed.
        """
        while True:
            self.battery = self.drone.get_battery()
            self.velocity = [self.drone.get_speed_x(), self.drone.get_speed_y(), self.drone.get_speed_z()]
            self.acceleration = [self.drone.get_acceleration_x(), self.drone.get_acceleration_y(), self.drone.get_acceleration_z()]
            self.orientation = [self.drone.get_roll(), self.drone.get_pitch(), self.drone.get_yaw()]
            self.altitude = self.drone.get_height()

            # Update at 10Hz
            sleep(0.1)

    def execute_path(self, path: list):
        """This function must be called to execute a path. Path is a set of waypoints only. For executing a set of Poses refer to another function 
        The Tello library doesnot give explicit command to cancel a command. So it will be better the waypoints in the path
        are small increments rather than long straight lines.
        """
        print(f"Executing Path with {len(path)-1}")
        self.state = "ExectuingPath"
        waypoints = [[path[i+1][0] - path[i][0], path[i+1][1] - path[i][1], path[i+1][2] - path[i][2]] for i in range(len(path)-1)]
        try:
            for waypoint in waypoints:
                print(f"Going to Waypoint {waypoint[0]}, {waypoint[1]}, {waypoint[2]}")
                self.drone.go_xyz_speed(*waypoint, self.safe_altitude)

            return True

        except Exception as e:
            # Go to a safety function
            self.safety_function()
            return False

    def execute_pose_path(self, poses: list):
        pass

    def __init_controller__(self):
        """Function that takes the Drone off and will make it ready for executing poses"""

        # Start the data collection thread
        self.data_thread.start()
        sleep(1)

        # Takeoff
        if self.battery > 35:
            self.drone.takeoff()
        else:
            # Check if the data is getting updated or not
            if self.acceleration != [0, 0, 0]:
                raise Exception(f"Battery is {self.battery}. Cannot takeoff if battery less than 35")
            else:
                raise Exception(f"Data Not being updated..")

        sleep(1)

        self.state = "Ready"

    def safety_function(self):
        self.state = "SafetyManuever"

        self.drone.land()





    


