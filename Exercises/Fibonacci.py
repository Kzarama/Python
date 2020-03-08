def fib(n):
	a, b = 0,1
	while a < n:
		if a%2 == 0:
			print(a, end='* ')
		else:
			print(a, end=' ')
		a, b = b, a+b
	print()
fib(50)