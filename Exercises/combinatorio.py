# Combinatorial between two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
numA = a
numB = b
c = numA - numB
factorialA = 1
factorialB = 1
factorialC = 1
for a in range (a,0,-1):
	factorialA *= a;
for b in range (b,0,-1):
	factorialB *= b;
for c in range (c,0,-1):
	factorialC *= c
combinatorial = (factorialA/(factorialC*factorialB))
print ("The combinatorial is: ", combinatorial)