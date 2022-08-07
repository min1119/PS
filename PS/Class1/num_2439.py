#별찍기 - 2
x=int(input())
for i in range(1,x+1):
    b=("*"*i) 
    print(b.rjust(x)) #오른쪽 정렬
    