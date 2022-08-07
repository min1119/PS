#알파벳 찾기
str1=input()
X=list(range(97,123))
for x in X:
    print (str1.find(chr(x)),end=" ")