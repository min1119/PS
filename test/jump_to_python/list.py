#리스트 인덱싱
a = [1,2,3,4,5,['a','b','c']]
print(a[0])
print(a[-1])
print(a[-1][0])
#리스트 슬라이싱 (끝번호 포함x)
print(a[0:2])
print(a[2:])
#리스트 더하기 = 합치기, 곱하기 = 반복

#len함수 = 리스트 길이 구하기
print(len(a))
print(str(a[2])+("hi")) #str함수가 a[2]의 값인 3의 정수를 문자열로 반환후 문자열끼리 덧셈

#del 함수 - 리스트 요소 삭제 (슬라이싱으로 한꺼번에 삭제 가능)
b=[1,2,3]
del(b[:2])
print (b)  

#리스트 관련 함수 - append/sort/reverse/index/insert/remove/pop/count/extend
B=[1,2,3] ; B.append(4)
c=[1,4,3,2] ; c.sort() #정렬(알파벳 순도 가능)
print (c)
B.reverse() #역순
print(B)
d=[1,2,3] ; print(d.index(3)) #숫자 3의 위치는 d[2]이므로 2를 반환
d.insert(0,4) #0번째자리에 4를 삽입
d.pop(1) #d[1]값 돌려내고 리스트에서 삭제, empty일 경우 맨 마지막 돌려주고 삭제
print(d)
X=[1,2,3]
X.extend([4,5]) #extend는 리스트만 올 수 있음 
print (X)

