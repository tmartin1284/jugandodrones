#!/usr/bin/env python3
"""
Script simple usando djitellopy
Instalar con: pip install djitellopy
"""

from djitellopy import Tello
import time

def test_drone():
    """Prueba básica del drone"""

    drone = None
    print("🚀 Iniciando prueba del Tello Boost Combo...")

    try:
        # Conectar
        drone = Tello()
        print("📡 Conectando...")
        drone.connect()
        print("✓ Conectado")
        
        # Obtener información
        battery = drone.get_battery()
        print(f"🔋 Batería: {battery}%")
        
        # Obtener velocidad configurada (algunos Tello responden con decimal)
        speed = drone.send_read_command_float('speed?')
        print(f"⚡ Velocidad: {speed:.1f} cm/s")

        # Vuelo automático con confirmación previa
        print("\n⚠️  Vuelo automático disponible: despegue + aterrizaje")
        confirmacion = input("Escribe SI para ejecutar vuelo automático corto: ").strip()

        if confirmacion.upper() == "SI":
            print("\n🚁 Ejecutando vuelo automático...")
            drone.takeoff()
            time.sleep(2)
            drone.land()
            print("✓ Vuelo automático completado")
        else:
            print("ℹ️ Vuelo automático cancelado")
        
        # Prueba de vuelo simple (comentado por seguridad)
        print("\n🚁 Lista para despegar")
        print("Para volar descomenta las siguientes líneas:")
        print("""
        drone.takeoff()
        time.sleep(2)
        drone.move_forward(100)
        time.sleep(1)
        drone.rotate_clockwise(180)
        time.sleep(1)
        drone.move_forward(100)
        time.sleep(1)
        drone.land()
        """)
        
        # Descomentar para vuelo real:
        # drone.takeoff()
        # time.sleep(2)
        # drone.move_forward(100)
        # time.sleep(1)
        # drone.rotate_clockwise(180)
        # time.sleep(1)
        # drone.move_forward(100)
        # time.sleep(1)
        # drone.land()
        
        print("\n✓ Prueba completada")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nAsegúrate de que:")
        print("1. pip install djitellopy")
        print("2. El drone está encendido")
        print("3. Conectado a la red WiFi del drone")
    finally:
        if drone is not None:
            try:
                drone.end()
            except Exception:
                pass

if __name__ == '__main__':
    test_drone()
