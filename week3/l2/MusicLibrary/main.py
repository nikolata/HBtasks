from songs import Song
from playlist import Playlist
def main():
	s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", lenght="3:44")
	print(str(s))
	print(s.lenght(seconds=True))
	print(s.lenght(minutes=True))
	print(s.lenght(hours=True))
	print(s.lenght())

	code_songs = Playlist(name="Code", repeat=True, shuffle=False)
	s1 = Song(title="Doko Doko", artist="Kondio", album="Cherno", lenght="2:34")
	s2 = Song(title="Churuliike", artist="Azis", album="Guchek", lenght="6:13")
	s3 = Song(title="Leden kralica", artist="Azis", album="jik - tak", lenght="2:55")

	entry = [s,s1,s2,s3]
	code_songs.add_song(entry)
	for el in code_songs.d:
		print(el)
	code_songs.remove_song([s])
	for el in code_songs.d:
		print(el)
	print(code_songs.artist())
	print(code_songs.next_song())
	print(code_songs.next_song())



if __name__ == '__main__':
	main()