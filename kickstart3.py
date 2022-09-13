T=int(input())
for i in range(1,T+1):
    A,B=[int(s) for s in input().split(" ")]
    count=0
    for j in range(A,B+1):
        sum1 = 0
        pr = 1
        while j:
            sum1 += j % 10
            pr *= j%10
            j //= 10
        if pr%sum1==0:
            count+=1
    print("Case #{}: {}".format(i,count))