import os # operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'products,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products




# let users input
def user_input(products):
	while True:
		name = input('Please input the name of the products: ')
		if name == 'q':
			break
		price = input('Please input the price of the products: ')
		products.append([name, price])
	print(products)
	return products

#print all the purchase records
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', p[1])

#write to the file
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('products,price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('Yeah, we have found the file!')
		products = read_file(filename)

	else:
		print('Cannot find the file...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()
