#구구단 4단 출력하기

dan = int(input("단을 입력해주세요: "))
for i in range(1,10):
    print("%d x %d = %d"% (dan,i,dan*i))
