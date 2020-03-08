word = input()
k = int(input())
cipher = ""
for x in range(len(word)):
    l = ord(word[x])
    if (l > 47 and l < 54):
        cipher += str(chr(l + k))
    elif(l > 53 and l < 58):
        cipher += str(chr(l - (k + 2)))
    elif(l > 64 and l < 87):
        cipher += str(chr(l + k))
    elif(l > 86 and l < 90):
        cipher += str(chr(l - (k + 18)))
    elif (l > 95 and l < 119):
        cipher += str(chr(l + k))
    elif (l > 118 and l < 122):
        cipher += str(chr(l - (k + 18)))
    else:
        cipher += str(chr(l))
print(cipher)