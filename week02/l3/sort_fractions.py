#sort_fractions

def validate_entry(fraction,ascending = True):
	if isinstance(fraction,list) == False:
		return False
	if ascending != True and ascending != False:
		return False

	for el in fraction:
		if isinstance(el,tuple) == False or isinstance(el[0],int) == False or isinstance(el[1],int) == False or len(el)!=2:
			return False
	return True
def sort_fraction(fraction, ascending = True):
	base = 0
	
	for i in range(len(fraction)):
		minn = fraction[i][0]/fraction[i][1]
		min_index = i
		for j in range(i+1,len(fraction)):
			if minn>fraction[j][0]/fraction[j][1]:
				minn= fraction[j][0]/fraction[j][1]
				min_index = j
		fraction[i],fraction[min_index] = fraction[min_index],fraction[i]
				
	if ascending ==True:
		return fraction
	else:
		return fraction[::-1]



def main():
	start = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
	ascending = False
	if validate_entry(start,ascending) == True:
		print(sort_fraction(start,ascending))

if __name__ == '__main__':
	main()