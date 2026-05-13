#!/usr/bin/env python3
"""Ejemplo: vuelo simple (secuencia preparada, no ejecutada por seguridad)."""

from djitellopy import Tello
import time


def main():
    print("\nEJEMPLO: Vuelo Simple")
    print("-" * 50)
    print("REQUIERE ESPACIO ABIERTO Y SEGURO")

    drone = Tello()
    drone.connect()

    print(f"Bateria: {drone.get_battery()}%")
    if drone.get_battery() < 40:
        print("Bateria muy baja para volar")
        drone.end()
        return

    try:
        # Descomenta para ejecutar vuelo real:
        # print("Despegando...")
        # drone.takeoff()
        # time.sleep(2)

        # print("Avanzando 100cm...")
        # drone.move_forward(100)
        # time.sleep(1)

        # print("Aterrizando...")
        # drone.land()

        print("Secuencia de vuelo lista (descomenta para ejecutar)")

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
