from pytube import YouTube
def descargarCancion(url:str):
    youtube=YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()

descargarCancion("https://www.youtube.com/watch?v=wohwc9MQt6A")