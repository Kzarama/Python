numberS = input()
sum = 0
for x in range(len(numberS)):
    sum += int(numberS[x]) * (x+1)
if(sum % 11 == 0):
    print("Legal ISBN")
else:
    print("Illegal ISBN")