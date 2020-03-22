import sys


def summ(arguments):
	s = 0
	temp = ''
	with open(arguments, "r") as f:
		string = f.read()
		print(string)
		for el in string:
			if el != ' ':
				temp = temp + el
			if el == ' ':
				s = s + int(temp)
				temp = ''
	print (s)


def main():
    summ(sys.argv[1])

if __name__ == '__main__':
    main()