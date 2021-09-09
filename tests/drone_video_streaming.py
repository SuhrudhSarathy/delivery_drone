"""Run the video capture in a separate thread and the movement in a separate thread"""
import cv2
from djitellopy import Tello as Drone
from threading import Thread
from time import sleep

class MyDrone:
    def __init__(self, camera_enabled=True):
        self.camera_enabled = camera_enabled
        self.drone = Drone()
        self.drone.connect()

        if self.camera_enabled:
            self.__init__stream__()

        self.drone.takeoff()

    def __init__stream__(self):
        # Initialises stream and shows it in a OpenCV Window
        self.stream_obj = self.drone.get_frame_read()
        self.keep_showing = True

        self.video_thread = Thread(target=self.show_video)
        self.video_thread.start()

    def show_video(self):
        while self.keep_showing:
            frame = self.stream_obj.frame

            cv2.imshow("Drone Stream", frame)

            if cv2.waitKey(1) == 0 and 0xFF == ord("q"):
                self.keep_showing = False
                
                self.land()

    def land(self):
        """Shut down all the threads and Land calmly"""

        self.drone.land()
        self.video_thread.join()

        print("Terminated Perfectly")

if __name__ == "__main__":
    drone = MyDrone(True)

    sleep(20)

    drone.land()

    

