from djitellopy import Tello
import time

drone = Tello()

time.sleep(5)

drone.connect()

print(drone.get_battery())