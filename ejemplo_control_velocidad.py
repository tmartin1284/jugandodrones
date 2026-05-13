#!/usr/bin/env python3
"""Ejemplo: control de velocidad del Tello."""

from djitellopy import Tello
import time


def main():
    print("\nEJEMPLO: Control de Velocidad")
    print("-" * 50)

    drone = Tello()
    drone.connect()

    print("Velocidades disponibles: 10-100 cm/s")

    try:
        # Descomenta para ejecutar vuelo real:
        # drone.set_speed(50)
        # print(f"Velocidad actual: {drone.get_speed()} cm/s")

        # drone.takeoff()
        # time.sleep(1)

        # print("Moviendo a velocidad lenta...")
        # drone.set_speed(30)
        # drone.move_forward(50)
        # time.sleep(1)

        # print("Moviendo a velocidad rapida...")
        # drone.set_speed(80)
        # drone.move_forward(50)
        # time.sleep(1)

        # drone.land()

        print("Control de velocidad listo (descomenta para ejecutar)")

    except Exception as e:
        print(f"Error: {e}")
        try:
            drone.land()
        except Exception:
            pass
    finally:
        drone.end()


if __name__ == "__main__":
    main()
