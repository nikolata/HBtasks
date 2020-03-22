#first

import sys

def cat(arguments):
    with open("{}.txt".format(arguments),"r") as f:
    	print(f.read())

def main():
    cat(sys.argv[1])

if __name__ == '__main__':
    main()