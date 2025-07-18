# 🎵 YT Downloader

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![Audio](https://img.shields.io/badge/Audio-MP3-orange?style=for-the-badge)
![Video](https://img.shields.io/badge/Video-MP4-blue?style=for-the-badge)

_¡Descarga videos y audio de YouTube de manera fácil y rápida!_

</div>

## 📋 Descripción

**YT Downloader** es una herramienta de línea de comandos desarrollada en Python que te permite descargar videos de YouTube en diferentes calidades o extraer únicamente el audio en formato MP3. Es simple, eficiente y fácil de usar.

## ✨ Características

- 🎥 **Descarga de videos** en calidades 720p y 1080p
- 🎵 **Extracción de audio** en formato MP3 de alta calidad (192 kbps)
- 📂 **Selección de directorio** personalizado para guardar archivos
- 🔧 **Limpieza automática** de nombres de archivo para evitar caracteres problemáticos
- 💻 **Interfaz intuitiva** con menú interactivo
- 🚀 **Rápido y confiable** usando yt-dlp

## 🛠️ Requisitos

Antes de usar YT Downloader, asegúrate de tener instalado:

- **Python 3.6+**
- **FFmpeg** (para procesamiento de audio/video)
- **yt-dlp** (se instala automáticamente)

## 📥 Instalación

1. **Clona este repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/yt_downloader.git
   cd yt_downloader
   ```

2. **Instala las dependencias:**

   ```bash
   pip install yt-dlp
   ```

3. **Instala FFmpeg:**
   - **Windows:** Descarga desde [FFmpeg.org](https://ffmpeg.org/download.html)
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt install ffmpeg` (Ubuntu/Debian)

## 🚀 Uso

1. **Ejecuta el programa:**

   ```bash
   python yt-downloader/yt-downloader.py
   ```

2. **Selecciona una opción del menú:**

   ```
   Bienvenido a YT Downloader
   1. Descargar video de YouTube
   2. Descargar audio de YouTube
   0. Salir
   ```

3. **Para descargar video:**

   - Ingresa la URL del video de YouTube
   - Selecciona la calidad (720 o 1080)
   - Especifica la ruta de descarga (opcional)

4. **Para descargar audio:**
   - Ingresa la URL del video de YouTube
   - Especifica la ruta de descarga (opcional)

## 📖 Ejemplos de Uso

### Descarga de Video

```
Seleccione una opción: 1
Ingresa la URL del video de YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Elige una calidad (720 o 1080): 1080
Ingrese la ruta donde desea almacenar el archivo de video: /ruta/a/mis/videos
```

### Descarga de Audio

```
Seleccione una opción: 2
Ingresa la URL del video de YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Ingrese la ruta donde desea almacenar el archivo de audio: /ruta/a/mi/musica
```

## 📁 Estructura del Proyecto

```
yt_downloader/
├── yt-downloader/
│   └── yt-downloader.py    # Archivo principal del programa
└── README.md               # Este archivo
```

## ⚙️ Funcionalidades Técnicas

- **Limpieza de nombres:** Elimina automáticamente caracteres no válidos (`\/*?:"<>|`) de los nombres de archivo
- **Gestión de rutas:** Permite especificar rutas personalizadas o usar el directorio actual
- **Calidad de audio:** Extrae audio en MP3 a 192 kbps de calidad
- **Formato de video:** Descarga en MP4 con la mejor calidad disponible
- **Interfaz clara:** Menú interactivo con limpieza de pantalla automática

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes ideas para mejorar el proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## ⚠️ Advertencias

- Respeta los derechos de autor y las políticas de YouTube
- Usa esta herramienta solo para contenido que tengas derecho a descargar
- Algunos videos pueden estar bloqueados por restricciones geográficas o de copyright

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 🆘 Solución de Problemas

### Error: "FFmpeg not found"

- **Solución:** Instala FFmpeg y asegúrate de que esté en tu PATH

### Error de descarga

- **Solución:** Verifica que la URL sea válida y que el video sea público

### Problemas con caracteres especiales

- **Solución:** El programa automáticamente limpia los nombres de archivo

---

<div align="center">
  
**¡Disfruta descargando tu contenido favorito de YouTube! 🎉**

Si te gusta este proyecto, ¡dale una ⭐!

</div>
