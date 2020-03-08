test = int(input())
list = list(map(int, input().split()))
val = 1
for x in range(test):
    val = (val * list[x]) % 1000000007
print(val)