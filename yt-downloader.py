import os
import yt_dlp
import re

def download_audio_from_youtube(video_url):
    output_path = input("Ingrese la ruta donde desea almacenar el archivo de audio (deje vacio para la carpeta actual): ").strip()
    if not output_path:
        output_path = "."  # Directorio actual
    output_path = os.path.join(output_path, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,  # Usar la ruta proporcionada por el usuario
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_title = info_dict.get('title', 'audio_sin_nombre')
        audio_file = f"{video_title}.mp3"

    clean_audio_file = re.sub(r'[\\/*?:"<>|]', "", audio_file)
    full_path = os.path.join(os.path.dirname(output_path), clean_audio_file)
    
    if os.path.exists(audio_file) and audio_file != full_path:
        os.rename(audio_file, full_path)
    
    print(f"El audio '{video_title}' ha sido descargado en '{full_path}'.")
    return full_path, video_title

def download_video_from_youtube(video_url, quality):
    output_path = input("Ingrese la ruta donde desea almacenar el archivo de video (deje vacio para la carpeta actual): ").strip()
    if not output_path:
        output_path = "."  # Directorio actual
    output_path = os.path.join(output_path, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': f'bestvideo[height={quality}]+bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_title = info_dict.get('title', 'video_sin_nombre')
        video_file = f"{video_title}.mp4"

    clean_video_file = re.sub(r'[\\/*?:"<>|]', "", video_file)
    full_path = os.path.join(os.path.dirname(output_path), clean_video_file)
    
    if os.path.exists(video_file) and video_file != full_path:
        os.rename(video_file, full_path)
    
    print(f"El video '{video_title}' ha sido descargado en {quality}p en '{full_path}'.")
    return full_path, video_title  

def mostrar_menu():
    print("Bienvenido a YT Downloader")
    print("1. Descargar video de YouTube")
    print("2. Descargar audio de YouTube")
    print("0. Salir")

if __name__ == "__main__":
    first = True
    while True:
        if(first):
            mostrar_menu()
            first = False
        else:
            input("Presiona enter para continuar: ")
            os.system('cls')
            mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            video_url = input("Ingresa la URL del video de YouTube: ")
            chosen_quality = input("Elige una calidad (720 o 1080): ").strip()
            download_video_from_youtube(video_url, chosen_quality)
        elif opcion == '2':
            url = input("Ingresa la URL del video de YouTube: ")
            download_audio_from_youtube(url)
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opcion invalida. Por favor, intente nuevamente.")