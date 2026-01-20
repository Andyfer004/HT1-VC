# HT1-VC — Procesamiento y segmentación simple de imágenes (Semana 1)

Este script aplica tres transformaciones a imágenes de ejemplo:

- Ajuste de contraste/brillo
- Corrección gamma
- Segmentación por rango HSV (rojo, verde, azul)

Los ejemplos de entrada están en la carpeta `ejemplos/` y los resultados se generan en `resultados/` (una subcarpeta por imagen con `contraste.png`, `gamma.png` y `segmentacion.png`).

## Estructura del repositorio

- `lab_semana1.py` — script principal en Python que contiene las funciones y el flujo de procesamiento.
- `requirements.txt` — dependencias utilizadas (OpenCV, NumPy, Matplotlib, Pillow, etc.).
- `ejemplos/` — imágenes de entrada de ejemplo.
- `resultados/` — carpetas generadas con las salidas por imagen.

## Requisitos

Fue desarrollado con Python 3.11.14 y requiere los paquetes listados en `requirements.txt`. Contenido (resumen):

```
contourpy
cycler
fonttools
kiwisolver
matplotlib
numpy
opencv-python
packaging
pillow
pyparsing
python-dateutil
six
```

Instala todo con pip:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Nota: si usas macOS y tienes problemas con la instalación de `opencv-python`, considera instalar primero las dependencias del sistema (por ejemplo, `brew install pkg-config jpeg libpng libtiff openexr tbb`), o usar una versión precompilada adecuada para tu entorno.

## Uso

Desde la raíz del proyecto (donde está `lab_semana1.py`) ejecuta:

```bash
python3 lab_semana1.py
```

El script hace lo siguiente:

- Lee todas las imágenes en `ejemplos/` con extensiones `.jpg`, `.jpeg` o `.png`.
- Para cada imagen crea una carpeta en `resultados/<nombre_de_imagen>/`.
- Aplica una transformación de contraste/brillo (alpha=1.2, beta=10) y guarda `contraste.png`.
- Aplica corrección gamma (gamma=0.6) y guarda `gamma.png`.
- Aplica segmentación en HSV sobre un color (rotando entre `rojo`, `verde`, `azul` según el índice de la imagen) y guarda `segmentacion.png`.

Durante la ejecución verás en consola líneas como:

```
mi_imagen.jpg -> segmentación verde
```
