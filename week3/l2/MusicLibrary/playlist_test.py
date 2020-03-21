import unittest
from playlist import Playlist
from songs import Song

class TestPlaylistClass(unittest.TestCase):
	def test_if_name_is_not_string_should_return_TypeError(self):
		entry = 123
		exc = None
		try:
			p = Playlist(name = entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Name should be a string')

	#add_song tests

	def test_if_add_song_element_is_not_list_should_return_TypeError(self):
		entry = 'this will give me error'
		p = Playlist(name = 'carl cox')
		exc = None
		try:
			p.add_song(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Should be a list of songs')
	def test_if_add_song_elements_are_not_Songs_should_return_TypeError(self):
		entry = [1,2,3]
		p = Playlist(name = 'carl cox')
		exc = None
		try:
			p.add_song(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be Songs!')
	def test_if_add_song_works(self):
		p = Playlist(name = '123')
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44')]
		p.add_song(k)

	#remove_songs tests
	def test_if_remove_song_element_is_not_list_should_return_TypeError(self):
		entry = 'this will give me error'
		p = Playlist(name = 'carl cox')
		exc = None
		try:
			p.remove_song(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Should be a list of songs')
	def test_if_remove_song_elements_are_not_Songs_should_return_TypeError(self):
		entry = [1,2,3]
		p = Playlist(name = 'carl cox')
		exc = None
		try:
			p.remove_song(entry)
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Elements need to be Songs!')
	def test_if_remvoe_song_is_in_our_list_returns_error_if_not(self):
		p = Playlist(name = 'carl cox')
		exc = None
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44')]
		p.add_song(k)
		m = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin3', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44')]
		try:
			p.remove_song(m)
		except Exception as err:
			exc = err
		self.assertRaises(KeyError)
	def test_if_remove_song_works(self):
		p = Playlist(name = 'carl cox')
		exc = None
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44')]
		p.add_song(k)
		m = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44')]
		p.remove_song(m)
	
	#total_length
	def test_if_total_length_return_the_same(self):
		p = Playlist(name = 'carl cox')
		exc = None
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44')]
		p.add_song(k)
		res =p.total_length()
		self.assertEqual(res,'0:9:28')

	#artist
	def test_if_there_are_no_songs_should_raise_error(self):
		p = Playlist(name = 'test')
		exc = None
		try:
			p.artist()
		except Exception as err:
			exc = err
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'There are no songs in the Playlist')
	def test_if_artist_return_the_same(self):
		p = Playlist(name = 'carl cox')
		exc = None
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44')]
		p.add_song(k)
		d = {'ManOWar':2}
		res = p.artist()
		self.assertEqual(res,d)
	#test next_song()

	def test_if_next_song_shuffle_next_song(self):
		p = Playlist(name = 'carl cox',repeat = False, shuffle = True)
		exc = None
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Ledena Kralica', artist = 'Azis', album = 'Lubov', lenght = '5:24')]
		p.add_song(k)
		p.next_song()
	def test_if_all_are_played_with_repeat_false(self):
		p = Playlist(name = 'carl cox',repeat = False, shuffle = True)
		exc = None
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Ledena Kralica', artist = 'Azis', album = 'Lubov', lenght = '5:24')]
		p.add_song(k)
		p.played = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Ledena Kralica', artist = 'Azis', album = 'Lubov', lenght = '5:24')]
		self.assertEqual(p.next_song(),'The Playlist is over')
	def test_if_all_are_played_with_repeat_True(self):
		p = Playlist(name = 'carl cox',repeat = True, shuffle = False)
		exc = None
		k = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Ledena Kralica', artist = 'Azis', album = 'Lubov', lenght = '5:24')]
		p.add_song(k)
		p.played = [Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Odin', lenght = '3:44'),Song(title = 'Odin', artist = 'ManOWar',album = 'The Sons Of Azis', lenght = '5:44'),\
		Song(title = 'Ledena Kralica', artist = 'Azis', album = 'Lubov', lenght = '5:24')]
		self.assertNotEqual(p.next_song(),'The Playlist is over')
	
if __name__ == '__main__':
	unittest.main()