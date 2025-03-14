products = []

while True:
	name = input('Please input the name of the products: ')
	if name == 'q':
		break
	price = input('Please input the price of the products: ')
	products.append([name, price])
print(products)
