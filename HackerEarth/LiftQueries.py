from sys import stdin, stdout

a = 0
b = 7
for x in range(int(stdin.readline())):
    floor = int(stdin.readline())
    if(abs(a - floor) <= abs(b - floor)):
        stdout.write("A\n")
        a = floor
    else:
        stdout.write("B\n")
        b = floor