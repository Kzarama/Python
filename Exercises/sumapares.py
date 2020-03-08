x = int(input("ingrese numero 1: "))
suma = 0
if x%2 == 0:
	while x < 101:
		suma += x
		x += 2
	print (suma)
else:
	x += 1
	while x < 101:
		suma += x
		x += 2
	print (suma)