products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'products,price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])

print(products)

while True:
	name = input('Please input the name of the products: ')
	if name == 'q':
		break
	price = input('Please input the price of the products: ')
	products.append([name, price])
print(products)

for p in products:
	print('The price of', p[0], 'is', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('products,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
