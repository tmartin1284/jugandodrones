#!/usr/bin/env python3
"""
Script de prueba para Drone Tello Boost Combo
Requiere: pip install djitellopy
"""

import socket
import time
from threading import Thread
from datetime import datetime

class TelloTest:
    def __init__(self, host='192.168.10.1', port=8889, timeout=5.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.running = False
        self.response = None
        
    def conectar(self):
        """Conectar con el drone"""
        try:
            print(f"[{self._timestamp()}] Intentando conectar con el drone en {self.host}:{self.port}...")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.settimeout(self.timeout)
            self.sock.bind(('', 9000))
            
            # Iniciar thread para recibir respuestas
            self.running = True
            recv_thread = Thread(target=self._recibir_respuestas, daemon=True)
            recv_thread.start()
            
            # Enviar comando de inicialización
            self.enviar_comando('command')
            time.sleep(1)
            
            print(f"[{self._timestamp()}] ✓ Conexión establecida")
            return True
            
        except Exception as e:
            print(f"[{self._timestamp()}] ✗ Error al conectar: {e}")
            return False
    
    def _recibir_respuestas(self):
        """Thread para recibir respuestas del drone"""
        while self.running:
            try:
                data, _ = self.sock.recvfrom(1024)
                self.response = data.decode('utf-8').strip()
            except socket.timeout:
                pass
            except Exception as e:
                if self.running:
                    print(f"[{self._timestamp()}] Error recibiendo: {e}")
    
    def enviar_comando(self, comando):
        """Enviar comando al drone"""
        try:
            print(f"[{self._timestamp()}] → {comando}")
            self.response = None
            self.sock.sendto(comando.encode('utf-8'), (self.host, self.port))
            time.sleep(0.3)
            
            if self.response:
                print(f"[{self._timestamp()}] ← {self.response}")
            return self.response
            
        except Exception as e:
            print(f"[{self._timestamp()}] ✗ Error enviando comando: {e}")
            return None
    
    def _timestamp(self):
        """Retorna timestamp formateado"""
        return datetime.now().strftime("%H:%M:%S")
    
    def desconectar(self):
        """Desconectar del drone"""
        self.running = False
        if self.sock:
            self.sock.close()
        print(f"[{self._timestamp()}] Desconectado")
    
    def ejecutar_pruebas(self):
        """Ejecutar suite de pruebas básicas"""
        print("\n" + "="*50)
        print("PRUEBAS DEL DRONE TELLO BOOST COMBO")
        print("="*50 + "\n")
        
        # Prueba 1: Obtener información del drone
        print("📋 PRUEBA 1: Información del Drone")
        print("-" * 50)
        self.enviar_comando('battery?')
        time.sleep(0.5)
        
        # Prueba 2: Prueba de vuelo simple (comentado por seguridad)
        print("\n🚁 PRUEBA 2: Secuencia de Vuelo (SIMULADO)")
        print("-" * 50)
        comandos_vuelo = [
            'takeoff',          # Despegar
            'forward 100',      # Avanzar
            'turn_cw 180',      # Girar 180°
            'forward 100',      # Avanzar de vuelta
            'land'              # Aterrizaje
        ]
        
        print("⚠️  Comandos de vuelo listos (no ejecutados por seguridad)")
        for cmd in comandos_vuelo:
            print(f"   • {cmd}")
        
        print("\nPara ejecutar el vuelo, descomenta las líneas en ejecutar_pruebas()")
        
        # Descomentar para ejecutar vuelo real:
        # for cmd in comandos_vuelo:
        #     self.enviar_comando(cmd)
        #     time.sleep(1)
        
        # Prueba 3: Pruebas de movimiento
        print("\n⬆️  PRUEBA 3: Movimientos Disponibles")
        print("-" * 50)
        movimientos = [
            'forward', 'backward', 'left', 'right',
            'up', 'down', 'turn_cw', 'turn_ccw'
        ]
        print("Movimientos disponibles:")
        for mov in movimientos:
            print(f"   • {mov} <distancia>")
        
        # Prueba 4: Información del sistema
        print("\n🔧 PRUEBA 4: Información del Sistema")
        print("-" * 50)
        comandos_info = [
            'battery?',    # Batería
            'speed?',      # Velocidad actual
            'time?'        # Tiempo de vuelo
        ]
        
        for cmd in comandos_info:
            self.enviar_comando(cmd)
            time.sleep(0.5)


def main():
    """Función principal"""
    tello = TelloTest()
    
    try:
        # Conectar con el drone
        if not tello.conectar():
            print("\n⚠️  No se pudo conectar. Asegúrate de:")
            print("   1. El drone está encendido")
            print("   2. Tu computadora está conectada a la red WiFi del drone")
            print("   3. El drone está en modo de reposo (no volando)")
            return
        
        # Ejecutar pruebas
        tello.ejecutar_pruebas()
        
        print("\n" + "="*50)
        print("✓ Pruebas completadas")
        print("="*50 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n⛔ Interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        tello.desconectar()


if __name__ == '__main__':
    main()
