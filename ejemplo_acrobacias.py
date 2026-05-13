#!/usr/bin/env python3
"""Ejemplo: acrobacias (flips) disponibles en Tello."""

from djitellopy import Tello
import time


def main():
    print("\nEJEMPLO: Acrobacias")
    print("-" * 50)
    print("REQUIERE ESPACIO ABIERTO Y SEGURO")

    drone = Tello()
    drone.connect()

    acrobacias_disponibles = [
        ("l", "Voltereta izquierda"),
        ("r", "Voltereta derecha"),
        ("f", "Voltereta adelante"),
        ("b", "Voltereta atras"),
    ]

    try:
        # Descomenta para ejecutar vuelo real:
        # print("Despegando...")
        # drone.takeoff()
        # time.sleep(2)

        # for comando, nombre in acrobacias_disponibles:
        #     print(f"Ejecutando: {nombre}...")
        #     drone.flip(comando)
        #     time.sleep(2)

        # print("Aterrizando...")
        # drone.land()

        print("Acrobacias disponibles:")
        for cmd, nombre in acrobacias_disponibles:
            print(f"- {nombre}: flip {cmd}")
        print("Acrobacias listas (descomenta para ejecutar)")

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
