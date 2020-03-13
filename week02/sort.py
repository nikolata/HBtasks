#sort.py

def allNumbersAreTheSame(iter = None, asc = True, key = None):
	same = True
	if key == None:
		for index in range(len(iter)-1):
			if iter[index] != iter[index+1]:
				same = False
	else:
		for index in range(len(iter)-1):
			if iter[index][key] != iter[index+1][key]:
				same = False
	if same == True:
		return True

def sortt(iter = None, asc = True, key = None):
	if allNumbersAreTheSame(iter,asc,key):
		return iter

	if len(iter)==0:
		return iter
	if len(iter)==1:
		return iter
	

	if asc == True:
		if key == None:
			n = len(iter)
			for i in range(n):
				for j in range(0, n-i-1):
					if iter[j] > iter[j+1] :
						iter[j], iter[j+1] = iter[j+1], iter[j]
			return iter
		else:
			n = len(iter)
			for i in range(n):
				for j in range(0, n-i-1):
					if iter[j][key] > iter[j+1][key] :
						iter[j], iter[j+1] = iter[j+1], iter[j]
			return iter


	elif asc == False:
		if key == None:
			n = len(iter)
			for i in range(n):
				for j in range(0, n-i-1):
					if iter[j] > iter[j+1] :
						iter[j], iter[j+1] = iter[j+1], iter[j]
			return iter[::-1]

		else:
			n = len(iter)
			for i in range(n):
				for j in range(0, n-i-1):
					if iter[j][key] > iter[j+1][key] :
						iter[j], iter[j+1] = iter[j+1], iter[j]
			return iter[::-1]

def return_sorted():
	pass


def main():
	pass

if __name__ == '__main__':
	main()
