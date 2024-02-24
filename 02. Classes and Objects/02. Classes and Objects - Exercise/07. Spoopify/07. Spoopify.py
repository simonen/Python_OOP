from project.song import Song
from project.album import Album
from project.band import Band

song = Song("Running in the 90s", 3.45, False)
song_chikina = Song("Chiki-na", 3.13, False)
print(song.get_info())
album = Album("Initial D", song, song_chikina)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
print()
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())