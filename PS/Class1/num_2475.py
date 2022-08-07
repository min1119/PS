#검증수
a,b,c,d,e=map(int,input().split())
KOI=a**2+b**2+c**2+d**2+e**2
print(KOI%10)

numlist=list(map(int,input().split()))
ans = 0
for i in numlist:
    print(i)
    ans+=i**2