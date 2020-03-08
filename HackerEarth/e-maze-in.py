inp = input()
x = 0
y = 0
for z in range(len(inp)):
    if(inp[z] == "L"):
        x += -1
    elif(inp[z] == "R"):
        x += 1
    elif(inp[z] == "U"):
        y += 1
    else:
        y += -1
print(f"{x} {y}")