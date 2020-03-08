'''
print(input().swapcase())
'''
'''
import sys
print(sys.stdin.readline().swapcase())
'''
'''
word = input()
newWord = ""
for x in range(len(word)):
    if(word[x].islower()):
        newWord += word[x].upper()
    else:
        newWord += word[x].lower()
print(newWord)
'''