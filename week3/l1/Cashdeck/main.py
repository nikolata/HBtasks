from cashdeck import Bill, BatchBill, CashDesk


def main():
	'''
	a = Bill(10)
	b = Bill(5)
	c = Bill(10)

	int(a) # 10
	str(a) # "A 10$ bill"
	print(a) # A 10$ bill

	print(a == b) # False
	print(a == c) # True

	money_holder= {}

	money_holder[a] = 1
	if c in money_holder:
		money_holder[c] += 1
	print(money_holder)
	'''
	'''
	values = [10, 20, 50, 100]
	bills = [Bill(value) for value in values]

	batch = BatchBill(bills)
	print(batch.__len__())
	print(batch.total())
	for bill in batch:
		print(bill)
	#print(batch)
	'''
	
	values = [10, 20, 50, 100, 100, 100]
	bills = [Bill(value) for value in values]

	batch = BatchBill(bills)

	desk = CashDesk()

	desk.take_money(batch)
	desk.take_money(Bill(10))
	print(desk.total())
	desk.inspect()
if __name__ == '__main__':
	main()