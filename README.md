# 🎨 Informática Gráfica y Visión por Computador (Python)

Tres prácticas de gráficos por computador y procesamiento de imagen con **Python, OpenGL y OpenCV**. Cada una tiene su código y su memoria técnica.

> Proyecto académico de la asignatura *Informática Gráfica y Visualización* (Grado en Ingeniería Informática).

## 📁 Contenido

### 1. Visualización de datos con OpenGL · `01_visualizacion_datos_opengl/`
Aplicación que lee un CSV de estaciones de servicio y dibuja **desde cero**, con primitivas OpenGL y GLUT, un **gráfico circular** de gasolineras por marca y un **gráfico de barras** con los 15 códigos postales con más estaciones. Incluye leyendas, texto y control por teclado.

### 2. Escena 3D con múltiples *viewports* · `02_escena_3d_opengl/` *(trabajo en equipo)*
Escena tridimensional modelada por objetos (mesa, sofá…) con iluminación y **cuatro vistas simultáneas**: perspectiva, planta, alzado y perfil.

### 3. Detección de contornos con OpenCV · `03_contornos_opencv/`
Generación de imágenes sintéticas con figuras geométricas, **umbralización**, **histogramas** y comparación cuantitativa de las estrategias de detección de contornos (`CHAIN_APPROX_NONE` y `CHAIN_APPROX_SIMPLE`).

## 🛠️ Tecnologías

Python 3 · PyOpenGL · GLUT/GLU · OpenCV · NumPy · Jupyter

```bash
pip install PyOpenGL PyOpenGL_accelerate opencv-python numpy
```

---
👤 Carlos Gálvez Reguera
