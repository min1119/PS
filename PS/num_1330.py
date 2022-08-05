#-100000=<A,B=<100000
A,B=map(int,input().split()) #map(function,iterable)

if A<B:
    print("<")
elif A>B:
    print(">")
elif A==B:
    print("==")