from songs import Song
from utls import validate_len
import json
import random
class Playlist(Song):
	def __init__(self,*,name,repeat= False,shuffle = False):
		if isinstance(name,str) == False:
			raise TypeError('Name should be a string')
		self.name = name
		self.repeat = repeat
		self.shuffle = shuffle
		self.d = set()
		self.played=[]
	def add_song(self,songs):
		if isinstance(songs,list) == False:
			raise TypeError('Should be a list of songs')
		for el in songs:
			if isinstance(el,Song) == False:
				raise TypeError('Elements need to be Songs!')
		
		self.d.update(songs)
	def remove_song(self,songs):
		if isinstance(songs,list) == False:
			raise TypeError('Should be a list of songs')
		for el in songs:
			if isinstance(el,Song) == False:
				raise TypeError('Elements need to be Songs!')
		for el in songs:
			self.d.remove(el)
	def total_length(self):
		h =0
		m =0
		s =0
		for el in self.d:
			#print('{}:{}:{}'.format(el.lenght(hours = True),el.lenght(minutes = True),el.lenght(seconds = True)))
			h = h + int(el.lenght(hours = True))
			m = m + int(el.lenght(minutes = True))
			s = s + int(el.lenght(seconds = True))
		temp = '{}:{}:{}'.format(h,m,s)
		tot_l = validate_len(temp)
		return tot_l
	def artist(self):
		if len(self.d) == 0:
			raise ValueError('There are no songs in the Playlist')
		songs_dict = {}
		for el in self.d:

			if el.artist in songs_dict:
				songs_dict[el.artist] +=1
			else:
				songs_dict[el.artist] = 1

		return songs_dict

	def next_song(self):
		temp = list(self.d)
		if len(self.played) == len(temp):
			if self.repeat == True:
				self.played =[]
				if self.shuffle == True:
					i = random.randrange(0,len(temp),1)
					self.played.append(temp[i])
					return temp[i]
				else:
					self.played.append(temp[0])
					return temp[0]
			else:
				return f'The Playlist is over'
		if self.shuffle == True:
			i = random.randrange(0,len(temp),1)
			b = False
			while b == False:
				if self.played.count(temp[i]) == 0:
					self.played.append(temp[i])
					b = True
					return temp[i]
				else:
					i = random.randrange(0,len(temp),1)
		else:
			k = len(self.played)
			self.played.append(temp[k])
			return temp[k+1]

	def save(self):
		path ='/home/nikola/py/week3/l2/MusicLibrary/playlist-data/test.json'
		with open(path,'w') as f:
			for el in self.d:
				t = el.title.replace(' ','-')
				art = el.artist.replace(' ','-')
				alb = el.artist.replace(' ','-')
				l = el._Song__len.replace(' ','-')
				my_obj = {'title':t, 'artist':art,'album':alb,'length':l}
				#obj = [t,art,alb,l]
				json.dump(my_obj,f)
				
	def loadd(self):
		path ='/home/nikola/py/week3/l2/MusicLibrary/playlist-data/test.json'
		table = []
		#cant do this, need to ask Marto
		with open(path,'r') as f:
			pass
			#table.append(json.load(f))
			

