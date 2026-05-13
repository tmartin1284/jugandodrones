#!/usr/bin/env python3
"""Ejemplo: informacion basica del Tello."""

from djitellopy import Tello


def main():
    print("\nEJEMPLO: Informacion Basica")
    print("-" * 50)

    drone = Tello()
    drone.connect()

    try:
        print(f"Bateria: {drone.get_battery()}%")
        print(f"Temperatura: {drone.get_temperature()} C")
        print(f"Velocidad: {drone.get_speed()} cm/s")
        print(f"Altura: {drone.get_height()} cm")
    finally:
        drone.end()


if __name__ == "__main__":
    main()
