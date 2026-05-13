#!/usr/bin/env python3
"""
Ejemplos avanzados para Tello Boost Combo
Ejecuta solo las pruebas que necesites
"""

from djitellopy import Tello
import time
import cv2

def ejemplo_info_basica():
    """Obtener información básica del drone"""
    print("\n📋 EJEMPLO 1: Información Básica")
    print("-" * 50)
    
    drone = Tello()
    drone.connect()
    
    print(f"Batería: {drone.get_battery()}%")
    print(f"Temperatura: {drone.get_temperature()}°C")
    print(f"Velocidad: {drone.get_speed()} cm/s")
    print(f"Altura: {drone.get_height()} cm")
    
    drone.end()


def ejemplo_vuelo_simple():
    """Vuelo simple: despegar, moverse, aterrizar"""
    print("\n🚁 EJEMPLO 2: Vuelo Simple")
    print("-" * 50)
    print("⚠️  REQUIERE ESPACIO ABIERTO Y SEGURO")
    
    drone = Tello()
    drone.connect()
    
    print(f"Batería: {drone.get_battery()}%")
    if drone.get_battery() < 40:
        print("❌ Batería muy baja para volar")
        drone.end()
        return
    
    try:
        # DESCOMENTA para ejecutar:
        # print("Despegando...")
        # drone.takeoff()
        # time.sleep(2)
        
        # print("Avanzando 100cm...")
        # drone.move_forward(100)
        # time.sleep(1)
        
        # print("Aterrizando...")
        # drone.land()
        
        print("✓ Secuencia de vuelo lista (descomenta para ejecutar)")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        drone.land()
    finally:
        drone.end()


def ejemplo_patron_cuadrado():
    """Vuela en patrón cuadrado"""
    print("\n📐 EJEMPLO 3: Patrón Cuadrado")
    print("-" * 50)
    print("⚠️  REQUIERE ESPACIO ABIERTO Y SEGURO")
    
    drone = Tello()
    drone.connect()
    
    en_el_aire = False
    try:
        bateria = drone.get_battery()
        print(f"Batería: {bateria}%")

        confirmacion = input("Escribe SI para ejecutar el patrón cuadrado: ").strip()
        if confirmacion.upper() != "SI":
            print("ℹ️ Patrón cuadrado cancelado")
            return

        print("Despegando...")
        drone.takeoff()
        en_el_aire = True
        time.sleep(2)

        distancia = 100
        for i in range(4):
            print(f"Lado {i+1}...")
            drone.move_forward(distancia)
            time.sleep(1)
            drone.rotate_clockwise(90)
            time.sleep(1)

        print("Aterrizando...")
        drone.land()
        en_el_aire = False

        print("✓ Patrón cuadrado completado")

    except Exception as e:
        print(f"❌ Error: {e}")
        if en_el_aire:
            try:
                drone.land()
            except Exception:
                pass
    finally:
        drone.end()


def ejemplo_acrobacias():
    """Ejecutar acrobacias (flips)"""
    print("\n🎪 EJEMPLO 4: Acrobacias")
    print("-" * 50)
    print("⚠️  REQUIERE ESPACIO ABIERTO Y SEGURO")
    
    drone = Tello()
    drone.connect()
    
    acrobacias_disponibles = [
        ('flip_l', 'Voltereta Izquierda'),
        ('flip_r', 'Voltereta Derecha'),
        ('flip_f', 'Voltereta Adelante'),
        ('flip_b', 'Voltereta Atrás'),
    ]
    
    try:
        # DESCOMENTA para ejecutar:
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
            print(f"  • {nombre}: {cmd}")
        print("\n✓ Acrobacias listas (descomenta para ejecutar)")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        drone.land()
    finally:
        drone.end()


def ejemplo_video():
    """Capturar video desde la cámara del drone"""
    print("\n📹 EJEMPLO 5: Captura de Video")
    print("-" * 50)
    print("Requiere: pip install opencv-python")
    
    try:
        drone = Tello()
        drone.connect()
        
        # Activar stream de video
        drone.streamon()
        
        # Capturar 10 frames
        print("Capturando video...")
        for i in range(10):
            frame = drone.get_frame_read().frame
            print(f"  Frame {i+1}/10 - Tamaño: {frame.shape}")
            time.sleep(0.5)
        
        drone.streamoff()
        print("✓ Video capturado correctamente")
        
        drone.end()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("¿Instalaste opencv-python? pip install opencv-python")


def ejemplo_control_velocidad():
    """Controlar velocidad del drone"""
    print("\n⚡ EJEMPLO 6: Control de Velocidad")
    print("-" * 50)
    
    drone = Tello()
    drone.connect()
    
    print("Velocidades disponibles: 10-100 cm/s")
    
    try:
        # DESCOMENTA para ejecutar:
        # drone.set_speed(50)  # 50 cm/s
        # print(f"Velocidad actual: {drone.get_speed()} cm/s")
        
        # drone.takeoff()
        # time.sleep(1)
        
        # print("Moviendo a velocidad lenta...")
        # drone.set_speed(30)
        # drone.move_forward(50)
        # time.sleep(1)
        
        # print("Moviendo a velocidad rápida...")
        # drone.set_speed(80)
        # drone.move_forward(50)
        # time.sleep(1)
        
        # drone.land()
        
        print("✓ Control de velocidad listo (descomenta para ejecutar)")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        drone.end()


def menu_principal():
    """Menú interactivo"""
    print("\n" + "="*50)
    print("EJEMPLOS AVANZADOS - TELLO BOOST COMBO")
    print("="*50)
    
    print("\nEscritos los ejemplos. Para ejecutarlos, descomenta las líneas")
    print("correspondientes en cada función.\n")
    
    ejemplos = [
        ("1", "Información Básica", ejemplo_info_basica),
        ("2", "Vuelo Simple", ejemplo_vuelo_simple),
        ("3", "Patrón Cuadrado", ejemplo_patron_cuadrado),
        ("4", "Acrobacias", ejemplo_acrobacias),
        ("5", "Captura de Video", ejemplo_video),
        ("6", "Control de Velocidad", ejemplo_control_velocidad),
        ("0", "Salir", None),
    ]
    
    for opcion, nombre, _ in ejemplos:
        print(f"  {opcion}. {nombre}")
    
    choice = input("\nSelecciona una opción (0-6): ").strip()
    
    for opcion, nombre, func in ejemplos:
        if choice == opcion:
            if func:
                try:
                    func()
                except KeyboardInterrupt:
                    print("\n⛔ Interrumpido por el usuario")
                except Exception as e:
                    print(f"\n❌ Error: {e}")
            break
    else:
        if choice != "0":
            print("❌ Opción no válida")


if __name__ == '__main__':
    menu_principal()
