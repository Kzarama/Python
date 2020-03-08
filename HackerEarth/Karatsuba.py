def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = int(m / 2)

        a = int(x / 10**(m2))
        b = int(x % 10**(m2))
        c = int(y / 10**(m2))
        d = int(y % 10**(m2))

        z0 = int(karat(b,d))
        z1 = int(karat((a+b),(c+d)))
        z2 = int(karat(a,c))

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

num1 = 74554548464451347578456
num2 = 474654464546513

karatsuba = karat(num1, num2)
v_num = num1 * num2
print(karatsuba, karatsuba == v_num)