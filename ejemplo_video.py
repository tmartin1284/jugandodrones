#!/usr/bin/env python3
"""Ejemplo: captura de video desde la camara del Tello."""

from djitellopy import Tello
import time


def main():
    print("\nEJEMPLO: Captura de Video")
    print("-" * 50)
    print("Requiere opencv-python instalado")

    drone = Tello()
    drone.connect()

    try:
        drone.streamon()
        print("Capturando video...")
        for i in range(10):
            frame = drone.get_frame_read().frame
            print(f"Frame {i + 1}/10 - Tamano: {frame.shape}")
            time.sleep(0.5)

        drone.streamoff()
        print("Video capturado correctamente")

    except Exception as e:
        print(f"Error: {e}")
        print("Instala dependencias con: python -m pip install -r requirements.txt")
    finally:
        drone.end()


if __name__ == "__main__":
    main()
