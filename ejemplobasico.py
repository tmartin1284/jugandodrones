from djitellopy import Tello
import time

tello = Tello()

# conectar
tello.connect()

print("Batería:", tello.get_battery())

# despegar
tello.takeoff()

# subir 50 cm
tello.move_up(50)

# esperar
time.sleep(2)

# aterrizar
tello.land()