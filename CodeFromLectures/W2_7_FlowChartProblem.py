print("Travel from City A to B Flowchart Based Problem")
time=int(input('Enter time : '))
longer=int(input('Define longer : '))
if(time >= longer):
	price=int(input('Enter Price : '))
	higher=int(input('Define higher : '))
	if(price >= higher):
		print('Train')
	else:
		print('Coach')
else:
	price=int(input('Enter Price : '))
	higher=int(input('Define higher : '))
	if(price >= higher):
		print('Daytime Flight')
	else:
		print('Red eye Flight')

print('You have arrived at city B.')
	
