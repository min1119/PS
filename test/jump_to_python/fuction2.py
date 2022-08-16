#결괏값은 언제나 하나여야함
from re import A
from tkinter import mainloop


def add_and_mul(a,b):
    return a+b, a*b 
result=add_and_mul(3,4) #하지만 결괏값이 두개여도 오류나지 않음-튜플값 하나로 돌려주기떄문
print(result)
result1,result2=add_and_mul(3,4)
print(result1,result2) #2개의 결괏값처럼 받음

#매개변수에 초깃값 미리 설정하기 man=True 맨 뒤쪽에 와야함
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다."% name)
    print("나이는 %d살 입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print('여자입니다.')
say_myself("박응용",27)
say_myself("박응용",27,True)
say_myself("박응선",27,False)

#함수 내에서 선언한 변수의 효력 범위 - 함수 안에서만 유효

#error.py
#def vartest(a):
    #a=a+1
#vartest(3)
#print(a) -> error

#함수 안에서 함수 밖의 변수를 변경하는 방법
#1.return 2.global(웬만하면 안쓰는게..) 3.lambda(def랑 동일한 역할)

a=1
def vartest(a):
    a=a+1
    return a
a=vartest(a)
print(a)

b=1
def vartest2():
    global b
    b+=1

vartest2()
print(b)

add = lambda a, b :a+b
result = add(3,4)
print(result)

    