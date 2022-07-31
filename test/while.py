#조건이 참인 동안 계속 반복
c=5
while c!=0:
    print(c)
    c-=1 #c-=1은 c에 -1해준 뒤 다시 할당 그러다보면 0이 됨
c=5
while c:
    print(c)
    c-=1
#break문
while True:
    a=input('숫자를입력하세요:')
    if int(a)%10==0:
        print('10으로 나누었을때 나머지가 0')
        break
#continue문 - 반복문 빠져나오지만 다음 코드 진행
while True:
    a =input('숫자를 입력하세요:')
    result = int(a)%10
    if result==0:
        continue
    print("10으로 나눈 나머지는 {} 입니다.".format(result))
