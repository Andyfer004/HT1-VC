# HT1-VC — Procesamiento y segmentación simple de imágenes (Semana 1)

Proyecto de prácticas para la asignatura (semana 1). Este script aplica tres transformaciones a imágenes de ejemplo:

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

El proyecto fue desarrollado para Python 3.8+ y requiere los paquetes listados en `requirements.txt`. Contenido (resumen):

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

### Parámetros y dónde modificarlos

Los parámetros están codificados en `lab_semana1.py`:

- Ajuste de contraste/brillo: `contrast_brightness(img, alpha=1.2, beta=10)`
- Gamma: `gamma_correction(img, gamma=0.6)`
- Orden de colores para segmentación: la lista `colors = ["rojo", "verde", "azul"]` determina qué color se usa para cada imagen según su índice.

Si quieres cambiar valores por defecto, edita `lab_semana1.py` o modifica el script para aceptar argumentos de línea de comandos (por ejemplo con `argparse`).

## Detalles de implementación

- `contrast_brightness` normaliza la imagen a [0,1], aplica `alpha * img + beta` y reescala a 0–255.
- `gamma_correction` aplica potencia por canal en espacio lineal (usando `np.power`).
- `hsv_segment` convierte la imagen a HSV y aplica un umbral por rangos predefinidos para `rojo`, `verde` y `azul`. El rojo se maneja con dos rangos (bajo y alto) para cubrir el wrap-around del espacio HSV.

## Resultados de ejemplo

La carpeta `resultados/` incluida contiene salidas de ejemplo ya generadas para las imágenes en `ejemplos/`:

- `resultados/ejemplo/` — contiene `contraste.png`, `gamma.png`, `segmentacion.png`.
- `resultados/ejemplo2/` — idem.
- `resultados/ejemplo3/` — idem.

Abre esas imágenes para comprobar visualmente los efectos.

## Problemas comunes y soluciones

- `cv2.imread` devuelve `None`: revisa la ruta de trabajo y que `ejemplos/` contiene archivos válidos. Ejecuta el script desde la raíz del proyecto.
- Errores de instalación de OpenCV en macOS: revisa dependencias del sistema o instala una versión compatible (por ejemplo usando `pip` dentro de un entorno virtual limpio).

## Contribuciones

Si quieres extender el proyecto, ideas rápidas:

- Añadir argumentos de línea de comandos para parámetros (alpha, beta, gamma, colores).
- Permitir elegir entre modos de segmentación (HSV, umbral por canal, k-means, etc.).
- Añadir visualización interactiva con Matplotlib o una pequeña UI.

Si añades mejoras, crea un commit claro y actualiza este README con ejemplos de uso.

## Licencia

Sin licencia especificada en el repositorio. Añade un archivo `LICENSE` si quieres publicar o compartir con condiciones concretas.

---

Si quieres, puedo:

- Añadir argumentos CLI al script (con `argparse`) y actualizar el README con ejemplos de uso.
- Crear un pequeño Notebook o script de demostración que muestre los resultados lado a lado.

Dime qué prefieres y lo implemento.
