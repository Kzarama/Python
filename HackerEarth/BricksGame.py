n=int(input())
count=0
cnt=0.0
for i in range(1,n+1):
    count+=i
    print(count)
    print(cnt)
    if(count+cnt>=n):
        print("Patlu")
        break
    cnt+=i*2
    if(count+cnt>=n):
        print("Motu")
        break