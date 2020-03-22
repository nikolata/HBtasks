#sort.py

def validate_entry(iterr,key = None):
	if iterr== None:
		raise TypeError('We need iterable')
	
	if isinstance(iterr,tuple) == False and isinstance(iterr,list)== False:	
		raise TypeError('Iterable should be tuple or list')
	if isinstance(iterr[0],dict) == False:
		if key != None:
			raise TypeError('Key can be added only if we have dicts')
		for el in iterr:
			if isinstance(el,int) == False:
				raise ValueError('Elements need to be integers')
	elif isinstance(iterr[0],dict):
		for i in range(0,len(iterr)-1):
			first = iterr[i].keys()
			second= iterr[i+1].keys()
			if first != second:
				raise ValueError('Keys need to be the same for all elements')
			first = [*iterr[i].values()]
			second = [*iterr[i+1].values()]
			for i in range(0,len(first)):
				if type(first[i]) != type(second[i]):
					raise TypeError('Values need to be the same type for all elements')


def sort(iterr = None, asc = True, key = None):
	if iterr !=None and len(iterr) == 0:
		return iterr
	validate_entry(iterr,key)
	is_tuple = False
	if isinstance(iterr,tuple):
		is_tuple = True
	if isinstance(iterr[0],dict) == False:
		iterr = list(iterr)
		for i in range(len(iterr)):
			min_indx = i
			for j in range(i+1,len(iterr)):
				if iterr[min_indx]>iterr[j]:
					min_indx = j
			iterr[i],iterr[min_indx] = iterr[min_indx],iterr[i]
	else:
		for i in range(len(iterr)):
			min_indx = i
			for j in range(i+1,len(iterr)):
				if iterr[min_indx][key]>iterr[j][key]:
					min_indx = j
			
			iterr[i],iterr[min_indx] = iterr[min_indx],iterr[i]

	if asc == True:
		if is_tuple:
			return tuple(iterr)
		return iterr
	else:
		if is_tuple:
			return tuple(iterr[::-1])
		return iterr[::-1]

def main():

	print(sort([]))
#[]
	print(sort((10,8,9,10,100)))
#(8, 9, 10, 10, 100)
	print(sort([10, 8, 9, 10, 100], False))
#[100, 10, 10, 9, 8]
	print(sort([{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}],True,'age'))
#[{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27


if __name__ == '__main__':
	main()
