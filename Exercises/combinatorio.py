a = int(input("INGRESE EL PRIMER NUMERO: "))
b = int(input("INGRESE EL SEGUNDO NUMERO: "))
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
combinarotio = (factorialA/(factorialC*factorialB))
print ("el combinatorio es: ", combinarotio)