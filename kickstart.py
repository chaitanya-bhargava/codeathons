def isDoable(str1,str2):
    for i in str1:
        for j in str2:
            if str[i]

if __name__==main:
    T=int(input())
    for i in range(T):
        I=input()
        P=input()
        count=0
        if (len(P)<len(I)):
            print(f"Case #{i+1}: IMPOSSIBLE")
        elif (len(P)==len(I) and P!=I):
            print(f"Case #{i+1}: IMPOSSIBLE")
        elif (I in P):
            count=len(P)-len(I)
            print(f"Case #{i+1}: {count}")
        elif()