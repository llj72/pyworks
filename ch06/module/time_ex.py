import time

print(time.time()) #1970년 1월 1일 자정 이후를 초로 환산

print(time.localtime())

print(time.ctime())  #날짜와 시간 요일 표시

print(time.strftime('%x', time.localtime()))

print(time.strftime('%c', time.localtime(time.time())))

#time.sleep(1) : 1초간 대기
for i in range(1,11):
    print(i)
    time.sleep(1)

