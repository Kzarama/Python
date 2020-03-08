word = input()
sum = 0
for x in range(len(word)):
    sum += ord(word[x]) - 96
print(sum)