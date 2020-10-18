products = []
#讀取檔案
with open ('products.csv', 'r', encoding='utf-8') as file:
	for line in file:
		if '商品名稱,商品價錢' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)
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
#印出購買紀錄
print(products)
for p in products:
	print('The price of', p[0], 'is', p[1])

#write to file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品名稱,商品價錢\n')
	for p in products:
		f.write(p[0] + ',' + (p[1]) + '\n')