#fractions_oop

class Fractions:
	def __init__(self,nom,den,ascending = True):
		self.nom = nom
		self.den = den
		self.ascending = ascending
	def validate_entry(self):
		
		if self.ascending != True and self.ascending != False:
			return False
		if isinstance(self.den,int) == False or isinstance(self.nom,int) == False or self.den==0 or self.nom == 0:
				return False
		return True

	def __add__(self,other):
		denom = self.den* other.den
		nom1 = self.nom * other.den
		nom2 = self.den * other.nom
		finalNom = nom1+nom2
		b = True
		while b == True:
			b = False
			for el in range(2,10):
				if denom%el==0 and finalNom%el ==0:
					denom = denom//el
					finalNom = finalNom//el
					b == True  
		summ = Fractions(finalNom,denom)
		#summ = (3,4)
		return summ

	def __eq__(self,other):
		if self.nom == other.nom and self.den == other.den:
			return True
		else:
			return False
	
	def __str__(self):
		return f'{self.nom}/{self.den}'

	def __repr__(self):
		return f' Fractions {self}'
	

	def get_largest_divisor(self):
		if self.nom != 1 and self.den != 1:
			minn = min(self.nom,self.den)
			i = minn
			for i in range(minn,1,-1):
				if self.nom%i==0 and self.den%i==0:
				
					return i
			return 1
		else:
			return 1
	def simplify_fraction(self):
		divisor = self.get_largest_divisor()
		final = Fractions(self.nom//divisor,self.den//divisor)
		return final

	@staticmethod
	def sort_fraction(fraction):
		for i in range(len(fraction)):
			minn = fraction[i].nom/fraction[i].den
			min_index = i
			for j in range(i+1,len(fraction)):
				if minn>fraction[j].nom/fraction[j].den:
					minn= fraction[j].nom/fraction[j].den
					min_index = j
			fraction[i],fraction[min_index] = fraction[min_index],fraction[i]
					
		return fraction

def main():
	f1  = Fractions(1,3)
	f2 = Fractions(1,2)
	f3 = Fractions(2,3)
	l = [f1,f2,f3]
	for el in l:
		if el.validate_entry() == False:
			return False

	f4 = f1 + f2
	print(f4)
	f5 = Fractions(3,9)
	f5 = f5.simplify_fraction()
	print(f5)

	print(f1.sort_fraction(l))

	#test = Fractions([(1,2),(3,4)])
if __name__ == '__main__':
	main()