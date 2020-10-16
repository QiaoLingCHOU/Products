products = []
while True:
	name = input('Please enter the name of the product:')
	if name == 'q':
		break
	price = input('Please enter the price of the product:')
	# p = []	
	# p.append(name)
	# p.append(price)
	# products.append(p)
	#simplify the codes
	#p = [name, price]
	#products.append(p)
	#simpligy the codes again
	products.append([name,price])
print(products)