from utls import validate_len,returnLen
class Song:
	def __init__(self,*,title,artist,album,lenght):
		if isinstance(title,str)== False or isinstance(artist,str)== False or\
		isinstance(lenght,str)== False or isinstance(album,str)== False:
			raise TypeError('Elements need to be string')
		if lenght.count(":") != 1 and lenght.count(":") != 2:
			raise TypeError('Lenght need to have atleast one ":"')
		self.title= title
		self.artist = artist
		self.album = album
		self.__len = validate_len(lenght)
	def __str__(self):
		return f'{self.artist} - {self.title} from {self.album} - {self.__len}'

	def __eq__(self,other):
		return self.title == other.title and self.artist == other.artist and\
		self.album == other.album and self.__len == other.__len

	def __hash__(self):
		return hash(self.title)
	def lenght(self,*,seconds = False,minutes = False,hours = False):
		temp = self.__len.split(':')
		tL = returnLen(temp)
		if seconds == True:
			return tL[2]
		if minutes == True:
			return tL[1]
		if hours == True:
			return tL[0]
		if seconds == False and minutes == False and hours == False:
			return self.__len
