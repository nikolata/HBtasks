def make_frames(entry):
	frames = []
	temp = []
	strike = 10
	is_used = False
	for i in range(0,len(entry)):
		if is_used == True:
			is_used = False
		else:
			if entry[i] == strike and i < len(entry)-3:
				frames.append([entry[i]])
			elif i>=len(entry)-3:
				temp.append(entry[i])
			elif i<len(entry)-3 and entry[i]!=strike:	
				frames.append([entry[i],entry[i+1]])
				is_used = True
	frames.append(temp)
	if len(frames) != 10:
		return f'invalid number of frames'
	for el in frames:
		if sum(el) >10 and len(el)!=3:
			raise ValueError('Pins need to be <= 10')
	return frames
def result(entry):
	frames = make_frames(entry)
	if isinstance(frames,str):
		return frames
	else:
		temp = []
		for i in range(0,len(frames)):
			if len(frames[i]) == 1:
				if len(frames[i+1]) !=1:
					temp.append(frames[i][0] + frames[i+1][0] + frames[i+1][1])
				if len(frames[i+1]) ==1:
					temp.append(frames[i][0] + frames[i+1][0] +frames[i+2][0])
			elif len(frames[i]) == 2:
				if frames[i][0] + frames[i][1] == 10:
					temp.append(frames[i][0] + frames[i][1] + frames[i+1][0])
				else:
					temp.append(frames[i][0] + frames[i][1])

			elif len(frames[i]) == 3:
				t = sum(frames[i])
				temp.append(t)

	return sum(temp)
