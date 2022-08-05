#key(불변):value(불변,가변)

#딕셔너리 쌍 추가
a={1:'a'}
a[2]='b'
a['name']='pey'
print(a) #a={1:'a',2:'b','name':'pey'}
print(a['name'])

#딕셔너리 요소 삭제
del a['name'] #a[key] 삭제
print(a)

#key로 value 반환 a[key]=value

#key에 list 불가능, tuple 가능
#b={[1,2]:'hi'} error

#딕셔너리 관련 함수 - keys/values/items/clear/get/in
dic={'name':'pey','phone':'123123','birth':'1119'}
print(dic.keys())     #key값만 얻음
print(list(dic.keys()))

for k in dic.keys():
    print(k)

print(dic.values()) #value값만 얻음

print(dic.items()) #key,value 쌍으로 얻음
#print(dic.clear()) 요소 모두 삭제

#get(x)함수
print(dic.get('name'))
print(dic.get('foo','bar')) #get(x,디폴트) 딕셔너리 안에 'foo'에 해당하는 value가 없으므로 디폴트 값인 'bar'를 반환

#in - 해당 key가 딕셔너리 안에 있는지 조사
print ('name' in dic) #true
    