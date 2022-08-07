#문자열 관련 함수 count/find/index/join/upper/lower/lstrip/rstrip/replace/split
a= "hobby"
print(a.count('b')) #개수
print(a.find('b')) #순서
print(a.index('b')) #b가 제일 먼저 나온 위치 반환
print(",".join("abcd"))
a="Life is too short"
print(a.replace("Life","Your leg"))
print(a.split()) #공백기준으로 문자열 나누어줌
b="a:b:c:d"
print(b.split(':')) #: 기준으로 문자열 나누어줌