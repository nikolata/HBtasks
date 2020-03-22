# cat2.py
import sys


def cat2(arguments):
    with open("{}".format(arguments),"r") as f:
    	print(f.read())

def main():
	temp = False
	for x in sys.argv:
		if temp == True:
			cat2(x)
		temp = True
if __name__ == '__main__':
    main()