from utls import result
class BowlingGame:
	def __init__(self,entry):
		if isinstance(entry,list) == False:
			raise TypeError('Entry should be a list')
		if len(entry) <11 or len(entry)>21:
			raise TypeError('Elements need to be between 11 and 21')
		for el in entry:
			if isinstance(el,int) == False or el<0:
				raise ValueError('Elements need to be positive integers')
			if el > 10:
				raise ValueError('Elements need to be between 0 and 10')
		self.entry = entry
		self.result = result(entry)


def main():
	game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
	print(game.result) # 65
	game = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
	print(game.result) # 0
	game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
	print(game.result) # 300
	game = BowlingGame([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])
	print(game.result) # invalid number of frame

if __name__ == '__main__':
	main()