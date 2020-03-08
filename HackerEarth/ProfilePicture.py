minimun = int(input())
test = int(input())
for x in range(test):
    numbers = list(map(int, input().split()))
    if (numbers[0] < minimun or numbers[1] < minimun):
        print("UPLOAD ANOTHER")
    elif(numbers[0] == numbers[1]):
        print("ACCEPTED")
    else:
        print("CROP IT")