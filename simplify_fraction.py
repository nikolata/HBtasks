#simplify_fraction

def validate_tuple(fraction):

	
	if len(fraction) == 0:
		raise ValueError('Tupple can not be empty')
	if len(fraction)==1:
		raise ValueError('Tupple need 2 arguments')
	if isinstance(fraction[0],int) == False or isinstance(fraction[1],int) == False:
		raise ValueError('Elements need to be integers') 
	if fraction[0]<=0 or fraction[1] <=0:
		raise ValueError('Arguments need to be positive')
	
def get_largest_divisor(fraction):
	if fraction[0] != 1 and fraction[1] != 1:
		minn = min(fraction[0],fraction[1])
		i = minn
		for i in range(minn,1,-1):
			if fraction[0]%i==0 and fraction[1]%i==0:
				
				return i
		return 1
	else:
		return 1
def simplify_fraction(fraction):
	divisor = get_largest_divisor(fraction)
	final = ()
	final = final + (fraction[0]//divisor,)
	final = final + (fraction[1]//divisor,)
	return final


def main():
	fraction = (123,8)
	validate_tuple(fraction)
	print(simplify_fraction(fraction))


if __name__ == '__main__':
	main()