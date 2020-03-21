def validate_len(lenght):
	temp = lenght.split(':')
	if len(temp) == 1:
		if int(temp[0]) >= 60:
			m = int(temp[0])//60
			s =int(temp[0])-m*60
			return '{}:{}'.format(m,s) 
	elif len(temp) == 2:
		if int(temp[1]) >= 60:
			m = int(temp[1])//60
			s =int(temp[1])-m*60
			temp[0] = int(temp[0]) + m
			temp[1] = s
		if int(temp[0]) >=60:
			h = 1
			temp[0] = temp[0]- 60
			return '{}:{}:{}'.format(h,temp[0],temp[1])
		return '{}:{}'.format(temp[0],temp[1])
	elif len(temp)==3:
		if int(temp[2]) >= 60:
			m = int(temp[2])//60
			s =int(temp[2])-m*60
			temp[1] = int(temp[1]) + m
			temp[2] = s
		if int(temp[1]) >=60:
			temp[0] = int(temp[0]) + 1
			temp[1] = temp[1]- 60
		return '{}:{}:{}'.format(temp[0],temp[1],temp[2])
def returnLen(temp):
	if len(temp)== 1:
		return ['0','0',temp[0]]
	elif len(temp) == 2:
		return ['0',temp[0],temp[1]]
	else:
		return [temp[0],temp[1],temp[2]]
