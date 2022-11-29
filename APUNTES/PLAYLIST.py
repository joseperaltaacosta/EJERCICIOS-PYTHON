from pytube import YouTube
def descargarCancion(url:str):
    youtube=YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()
#descargarCancion("https://www.youtube.com/watch?v=LALq7BIz3bk")


from pytube import Playlist
def descargarLista(url:str):
    playlist=Playlist(url)
    for cancion in playlist.videos:
        print("Descargando cancion:", cancion.title)
        cancion.streams.get_audio_only().download("CANCIONES/")
        print("***********\n")
url="https://www.youtube.com/watch?v=u-N0ABBfIpY&list=PLtjIbSCPIhb3d94DG4dR9vqM7bieaHZM4"
#vaya mierda cancion, ponme breakbeat
descargarLista(url)