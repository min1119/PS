#집합자료형 - 1.중복허용x 2.순서x(리스트,튜플은 순서o)
S1=set([1,2,3])
print(S1)
S2=set("hello")
print(S2)

#unordered라서 indexing하려면 리스트나 튜플로 변환 후
l1=list(S1) #리스트화
print(l1)
print(l1[0])
t1=tuple(S1) #튜플화
print(t1);print(t1[0])

#교집합,합집합,차집합 구하기
s1=set([1,2,3,4,5])
s2=set([4,5,6,7,8,9])
#교집합 &/.intersection()
print(s1&s2)
#합집합 \/.union()
print(s1.union(s2))
#차집합 -/.difference()
print(s1-s2)

#집합관련함수 - add(1개만 추가)/update(한꺼번에 추가)/remove
a=set([1,2,3])
a.add(4); print(a)
a.update([4,5,6]) ; print(a)
a.remove(2);print(a)