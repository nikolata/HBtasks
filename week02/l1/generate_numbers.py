# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename, numbers):
    with open("{}".format(filename),"w") as f:
	    for i in range(0,int(numbers)):
	    	f.write(str(randint(1,1000)))
	    	f.write(" ")



    



def main():
    generate_numbers(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()