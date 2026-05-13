## Inicio rapido

Antes de ejecutar los scripts, activa el entorno virtual e instala las dependencias:

```bash
cd /Users/pacopulido/Desktop/drone
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Si no existe `.venv`, crealo con:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

# 🚁 Script de Prueba - Drone Tello Boost Combo

Scripts para probar y controlar tu drone DJI Tello Boost Combo mediante Python.

## 📋 Requisitos

- Python 3.7+
- Drone Tello Boost Combo
- Conexión WiFi

## 🔧 Instalación

### Opción 1: Usando djitellopy (RECOMENDADO)
```bash
python3 -m pip install djitellopy
```

### Opción 2: Script manual (sin dependencias)
El archivo `test_tello.py` usa solo librerías estándar de Python.

## 📁 Archivos

### Scripts individuales (desde `ejemplos_avanzados.py`)

Estos scripts permiten ejecutar cada funcion por separado:

- `ejemplo_info_basica.py` - Estado basico (bateria, temperatura, velocidad, altura)
- `ejemplo_vuelo_simple.py` - Secuencia simple de vuelo (comentada por seguridad)
- `ejemplo_patron_cuadrado.py` - Vuelo en cuadrado con confirmacion `SI`
- `ejemplo_acrobacias.py` - Flips disponibles (comentados por seguridad)
- `ejemplo_video.py` - Captura de frames de video
- `ejemplo_control_velocidad.py` - Cambios de velocidad (comentado por seguridad)

**Uso rapido:**
```bash
python3 ejemplo_info_basica.py
python3 ejemplo_vuelo_simple.py
python3 ejemplo_patron_cuadrado.py
python3 ejemplo_acrobacias.py
python3 ejemplo_video.py
python3 ejemplo_control_velocidad.py
```

### `test_tello.py`
Script completo que NO requiere librerías externas. Usa conexión UDP directa.

**Características:**
- Conexión manual al drone por UDP
- Suite de pruebas básicas
- Obtiene información del drone (batería, velocidad, tiempo)
- Muestra comandos disponibles
- Incluye ejemplos de vuelo (comentados por seguridad)

**Uso:**
```bash
python3 test_tello.py
```

### `test_tello_simple.py`
Script simple usando la librería `djitellopy` (más fácil de usar).

**Características:**
- API más intuitiva
- Métodos simples para cada acción
- Acceso a información del drone

**Uso:**
```bash
python3 test_tello_simple.py
```

## 🚀 Cómo Usar

### Paso 1: Preparar el Drone
1. Enciende el drone Tello Boost Combo
2. El drone creará una red WiFi llamada `TELLO-XXXXX`
3. Conecta tu computadora a esa red WiFi

### Paso 2: Ejecutar Pruebas
```bash
# Opción A: Sin dependencias externas
python3 test_tello.py

# Opción B: Con djitellopy (si instalaste)
python3 test_tello_simple.py

# Opción C: Scripts individuales
python3 ejemplo_info_basica.py
python3 ejemplo_vuelo_simple.py
python3 ejemplo_patron_cuadrado.py
python3 ejemplo_acrobacias.py
python3 ejemplo_video.py
python3 ejemplo_control_velocidad.py
```

### Paso 3: Ver Información del Drone
Los scripts mostrarán:
- Estado de conexión
- Nivel de batería (%)
- Velocidad actual
- Comandos disponibles

## ⚡ Comandos Disponibles

### Movimiento
- `forward <cm>` - Avanzar
- `backward <cm>` - Retroceder
- `left <cm>` - Moverse a la izquierda
- `right <cm>` - Moverse a la derecha
- `up <cm>` - Subir
- `down <cm>` - Bajar
- `turn_cw <grados>` - Girar a la derecha (clockwise)
- `turn_ccw <grados>` - Girar a la izquierda (counter-clockwise)

### Control de Vuelo
- `takeoff` - Despegar
- `land` - Aterrizaje
- `flip_l` - Voltereta a la izquierda
- `flip_r` - Voltereta a la derecha

### Información
- `battery?` - Estado de batería
- `speed?` - Velocidad actual
- `time?` - Tiempo de vuelo

## ⚠️ ADVERTENCIAS DE SEGURIDAD

1. **Vuela en un área abierta** y despejada
2. **Asegura a las personas cercanas** - El drone tiene hélices rápidas
3. **Los comandos de vuelo están comentados** para evitar que se ejecuten accidentalmente
4. **Comienza con movimientos pequeños** para probar estabilidad
5. **Revisa la batería** antes de cada vuelo (mínimo 40%)
6. **Sigue las regulaciones locales** de drones

## 🛠️ Activar Vuelo Automático

Para ejecutar comandos de vuelo, descomenta las líneas correspondientes en los scripts:

### En `test_tello.py` (línea ~110):
```python
# Descomentar para ejecutar vuelo real:
for cmd in comandos_vuelo:
    self.enviar_comando(cmd)
    time.sleep(1)
```

### En `test_tello_simple.py` (línea ~30):
```python
# Descomentar para vuelo real:
drone.takeoff()
time.sleep(2)
drone.move_forward(100)
...
```

## 🐛 Troubleshooting

### "No se pudo conectar"
- ¿Está el drone encendido?
- ¿Está conectada tu computadora a la red WiFi del drone?
- ¿El drone muestra la red WiFi?

### "Connection timeout"
- El drone podría estar ocupado
- Intenta apagar y encender el drone
- Reinicia tu computadora

### "Permission denied" en Python
```bash
chmod +x test_tello.py
```

## 📚 Referencias

- [Documentación DJI Tello](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)
- [djitellopy GitHub](https://github.com/damiafuentes/DJITelloPy)

## 📝 Notas

- El primer script (`test_tello.py`) es más robusto para debugging
- El segundo script (`test_tello_simple.py`) es más fácil para programas complejos
- Los scripts `ejemplo_*.py` son utiles para probar funciones concretas por separado
- Mantén el drone a menos de 10 metros de distancia

---

¡Feliz vuelo! 🎮✈️
