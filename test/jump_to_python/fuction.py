#def 함수명(매개변수):
#   <수행할문장1>...
#   return 결과값
def add(a,b): #a,b는 매개변수
    return a+b
a=3;b=4;c=add(a,b) #a,b는 인수
print(c)

#매개변수: 함수에 입력으로 전달된 값을 받는 변수를 의미
#인수: 함수를 호출할 때 전달하는 입력값을 의미
#함수 - 일반적인 함수/입력값x함수/결과값x함수/둘다x함수
def add1(a,b):
    print("%d,%d의 합은 %d입니다."%(a,b,a+b))
a=add1(3,4)   #결과값이 없으므로 add1(3,4) 함수는 반환값으로 a 변수에 none을 돌려줌
def add2(a,b):
    return a+b
result1 =add(a=3,b=7) #매개변수 지정-순서 상관x
print(result1)

#입력값이 여러개 일 때(*)
def add_many(*args):
    result = 0
    for i in args:
        result=result+i
    return result
result=add_many(1,2,3)
print(result)

def add_mul(choice,*args):
    if choice == "add":
        result3 = 0
        for i in args:
            result3 = result3 + i
    elif choice == "mul":
        result3 = 1
        for i in args:
            result3 = result3 * i
    return result3
result3=add_mul("add",1,2,3,4,5)
print(result3)

result3=add_mul("mul",1,2,3,4,5)
print(result3)

#키워드 파라미터 kwargs ** 딕셔너리 화
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1) #{"a":1}
print_kwargs(name='foo',age=3) #{'age:3','name'='foo',age=3}