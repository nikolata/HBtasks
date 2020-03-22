import sys

def count(t,fn):
	with open(fn,"r") as f:
		string = f.read()
		count = 0
		if t == "chars":
			for el in string:
				#if el !=" ":
				count +=1
			return print(count)
		if t == "lines":
			
			count = len(open(fn).readlines(  ))
			return print(count)
		if t == "words":
			with open(fn) as fd:
				count = sum(1 for line in fd if len(line.strip()) == 0)

			for el in string:
				if el == " ":
					count +=1

			return print(count+1)


def main():
    count(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()