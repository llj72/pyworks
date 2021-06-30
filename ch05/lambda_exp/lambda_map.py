
li = [1, 2, 3, 4, 5]

li2 = map(lambda x : x * 3, li) #map(함수, 자료형)
print(list(li2))
print(list(map(lambda x : x *3, li)))

#4보다 작은 요소 추출
li3 = filter(lambda x : x < 4, li)
print(list(li3))