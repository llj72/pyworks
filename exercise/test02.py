#1번
국어 = 80
영어 =75
수학 = 55
sum = 국어 + 영어 + 수학
avg = sum / 3
print("평균:", avg)


#2번
#print("13나누기 2의 나머지", 13%2)

n = 13
if n%2 ==0:
    print("짝수")
else:
    print("홀수")


#3번
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print("생년월일 부분:",yyyymmdd)
print("숫자 부분:",num)

#4번
gender = pin[7]
if gender == "1":
    print("남자입니다.")
else:
    print("여자입니다.")

#5번
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

#6번
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)


#7번
a=['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#split() 예제
s = "Life is too short."
s=s.split(' ') #구분기호 : 공백
print(s)

s = 'a:b:c:d'
s=s.split(':')
print(s)

#8번
a = (1,2,3)
a = a+(4,)
print(a)

#9번
a = dict()
a['name']='python'
print(a)
a[('a',)]='python'
#print(a)
#a[[1]] = 'python'
print(a)
a[250]='python'
print(a)

#10번
a={'A':90, 'B':80, 'C':70}
result = a.pop('B') # 추출
print(a)
print(result)

#11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#12번
a = b= [1,2,3]
a[1]=4
print(b)
