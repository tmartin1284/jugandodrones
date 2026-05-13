#!/usr/bin/env python3
"""Ejemplo: patron cuadrado con confirmacion explicita."""

from djitellopy import Tello
import time


def main():
    print("\nEJEMPLO: Patron Cuadrado")
    print("-" * 50)
    print("REQUIERE ESPACIO ABIERTO Y SEGURO")

    drone = Tello()
    drone.connect()

    en_el_aire = False
    try:
        bateria = drone.get_battery()
        print(f"Bateria: {bateria}%")

        confirmacion = input("Escribe SI para ejecutar el patron cuadrado: ").strip()
        if confirmacion.upper() != "SI":
            print("Patron cuadrado cancelado")
            return

        print("Despegando...")
        drone.takeoff()
        en_el_aire = True
        time.sleep(2)

        distancia = 100
        for i in range(4):
            print(f"Lado {i + 1}...")
            drone.move_forward(distancia)
            time.sleep(1)
            drone.rotate_clockwise(90)
            time.sleep(1)

        print("Aterrizando...")
        drone.land()
        en_el_aire = False

        print("Patron cuadrado completado")

    except Exception as e:
        print(f"Error: {e}")
        if en_el_aire:
            try:
                drone.land()
            except Exception:
                pass
    finally:
        drone.end()


if __name__ == "__main__":
    main()
