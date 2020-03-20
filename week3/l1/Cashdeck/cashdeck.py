#cashdeck

class Bill:
	def __init__(self,money=0):
		if isinstance(money,int) == False:
			raise TypeError
		elif money<0:
			raise ValueError
		self.money = money

	def __int__(self):
		print(self.money)
		return int(self.money)
	def __str__(self):
		#print('"A {}$ bill"'.format(self.money))
		return f'"A {self.money}$ bill"'

	def __repr__(self):
		return f'A {self.money}$ bill'

	def __eq__(self,other):
		return self.money == other.money
	def __hash__(self):
		return hash(self.money)



class BatchBill:
	def __init__(self,listt):
		if isinstance(listt,list) == False:
			raise TypeError
		for el in listt:
			if isinstance(el,Bill) == False:
				raise TypeError
		self.listt= listt
	def __len__(self):
		return len(self.listt)
	def total(self):
		summ =0
		for i in range(0,len(self.listt)):
			summ = summ + self.listt[i].money
		return summ

	def __getitem__(self,key):
		return self.listt[key]

class CashDesk:
	def __init__(self,d = None,totall= 0):
		self.d = {}
	def take_money(self,bills):
		if isinstance(bills,BatchBill) == True:
			for b in bills:
				if b in self.d:
					self.d[b] +=1
				else:
					self.d[b] = 1
		elif isinstance(bills,Bill) == True:
			if bills in self.d:
				self.d[bills] +=1
			else:
				self.d[bills] = 1
		#print(self.d)

	def total(self):
		summ = 0
		i = 0
		c = [*self.d.values()]
		for el in self.d:
			summ = summ + el.money*c[i]
			i+=1
		self.totall= summ
		return summ

	def inspect(self):
		print('We have a total of {}$ in the desk'.format(self.totall))
		k = [*self.d.keys()]
		v = [*self.d.values()]
		print('We have the following count of bills, sorted in ascending order:')
		for i in range(0,len(self.d)):
			print('{} - {}'.format(k[i],v[i]))

