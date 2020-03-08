numbers = list(map(int, input().split()))
count = 0
for x in range(numbers[0], numbers[1] + 1):
    if(x % numbers[2] == 0):
        count += 1
print(count)