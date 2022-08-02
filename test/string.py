#여러열 문자 입력할떈 """/'''
print("""멀티라인입력
멀티라인입력""")

#이스케이프 문자
a="이스케이프 문자\n라인이바뀜\n쌍따옴표를 또 쓰기\"\""
print(a)
b=r"이스케이프 문자\n라인이바뀜\\쌍따옴표를 또 쓰기\"\""
print(b)

#collection
s='abcdef'
print(s[3])
a = [1,2,3,['a','b','c']]
print(a[-1][0]) #리스트a에 포함된 리스트에서 'a'값을 인덱싱,[시작번호:끝번호,단 끝번호 포함x]

#문자열 formatting 숫자 - %d, 문자열 - %s(사실 뭐든 문자열로 바꿔서 들어가게함)
print("I eat %d apples."%3)
print("I eat %s apples."%'five')
number = 3
print("I eat %d apples."%number)
num = 10 ; day="three"
print ("I ate %d apples. so I was sick for %s days."%(num,day))
#정렬과 공백
print("%10s"%"hi") #전체 길이가 10개인 문자열에서 대입값을 오른쪽으로 정렬 나머지 공백
print("%-10sjane."%"hi") #그 반대
print("%10.4f"%3.42134234) #소숫점 네 번째 자리까지 이하동문

#format 함수
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples".format(number))
print("I ate {0} apples.so I was sick for {1} days.".format(num,day))
print("I ate {n} apples.so I was sick for {d} days.".format(n=10,d=3))
name=이동민
print ("'my name is {name}'")