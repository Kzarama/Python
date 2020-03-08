from sys import stdin, stdout

for x in range(int(stdin.readline())):
    line = list(input().split())
    line1 = line[0]
    line2 = line[1]
    for z in range(len(line1)):
        if(line1[z] in line2):
            line2 = line2.replace(line1[z], "", 1)
            if(z == len(line1) - 1):
                stdout.write("YES\n")
        else:
            stdout.write("NO\n")
            break