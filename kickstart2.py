from random import randint
def isPalindrome(s):
    return s == s[::-1]
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        S=input()
        c=S.count('?')
        if N<5:
            y="IMPOSSIBLE"
        else:
            S2=S
            S3=S
            S4=S
            for k in range(c):
                S2=S2.replace('?','0')
                S3=S3.replace('?','1')
                S4=S4.replace('?',str(randint(0,2)))
            for j in range(N-4):
                if isPalindrome(S2[j:j+5]):
                    y="IMPOSSIBLE"
                    break
                elif isPalindrome(S3[j:j+5]):
                    y="IMPOSSIBLE"
                    break
                elif isPalindrome(S4[j:j+5]):
                    y="IMPOSSIBLE"
                    break
            else:
                y="POSSIBLE"
        print(f"Case #{i+1}: {y}")