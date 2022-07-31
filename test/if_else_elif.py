#관계연산자+조건절(IF)
if True:
    print("여기는 무조건 실행")
if False:
    print("여기는 무조건 실행안됨")
if bool("문자열"):
    print("문자열 값이 있으면 True")
if "문자열":
    print("문자열 값이 있으면 True")
if "":
    print ("문자열 값이 빈값이면 False, 실행안됨")
#else블럭
h=50
if h>50:
    print("50보다 크면 실행")
else:
    print("50과 같거나 작으면 실행")
#elif블럭
if h>50:
    print("50보다 크면 실행")
elif h<20:
    print("20보다 작으면 실행")
else:
    print("50과 같거나 작고, 20과 같거나 크면 실행")
