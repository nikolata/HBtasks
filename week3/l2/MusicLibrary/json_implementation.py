import json
from songs import Song
from playlist import Playlist


code = Playlist(name = 'Best hits')

s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", lenght="3:44")
s1 = Song(title="Doko Doko", artist="Kondio", album="Cherno", lenght="2:34")
s2 = Song(title="Churuliike", artist="Azis", album="Guchek", lenght="6:13")
s3 = Song(title="Leden kralica", artist="Azis", album="jik - tak", lenght="2:55")

entry = [s,s1,s2,s3]
code.add_song(entry)

code.save()

code.loadd()