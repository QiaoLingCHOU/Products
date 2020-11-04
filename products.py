import os #operating system
def read_file(filename):
	products = []
	with open (filename, 'r', encoding='utf-8') as file: #讀取檔案
		for line in file:
			if '商品名稱,商品價錢' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return products

def user_input(products):
	while True:
	    name = input('Please enter the name of the product:')
	    if name == 'q':
		    break
	    price = input('Please enter the price of the product:')
	    products.append([name,price])
	return products

#印出購買紀錄
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', p[1])

#write to file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
	    f.write('商品名稱,商品價錢\n')
	    for p in products:
		    f.write(p[0] + ',' + (p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('Yes, the file exit.')
		products = read_file(filename)
	else:
		print('No such file.')
	products = user_input(products)
	print_products(products)
	write_file('prodcuts.csv', products)
main()
