#비교 연산자 쓸때, =이 무조건 오른쪽. >=.<=

pocket=['paper','money','cellphone']
if 'moneny' in pocket: pass
else : print ("카드를 꺼내라")

treehit = 0
while treehit < 10:
    treehit+=1
    print('나무를 %d번 찍었습니다.'%treehit)
    if treehit == 10:
        print('나무 넘어갑니다.')

a=0
while a<10: #홀수만출력
    a+=1
    if a%2==0: continue #while 문의 맨 처음으로 돌아감
    print(a)
    
b=[(1,2),(3,4),(5,6)]
for (first,last) in b:
    print(first+last)

marks=[90,25,67,45,80]

number=0
for mark in marks:
    number+=1
    if mark>=60:
        print("{}번 학생은 합격입니다.".format(number))
    else :
        print("{}번 학생은 불합격입니다.".format(number))
        
#구구단
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ") #매개변수 end - 다음줄로 넘기지 않고 같은 줄에 계속 출력
    print('') 

#리스트 내포 사용
c =[1,2,3,4]
result=[]
for num in c:
    result.append(num*3)
print(result)

#짝수만 [표현식 for 항목 in 반복가능객체 if 조건문]
C=[1,2,3,4]
Result=[num*3 for num in C if num%2==0]
print(Result)

#구구단 with 리스트내포
RESULT=[x*y for x in range(2,10) 
            for y in range(1,10)]
print(RESULT)


        