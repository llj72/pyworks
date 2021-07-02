'''
with open('score.txt', 'a') as f:
    name = input("이름 입력 : ")
    kor = int(input("국어 점수 : "))
    math = int(input("수학 점수 : "))
    avg = (kor + math) /2

    f.write(name + ' ')
    f.write(str(kor) + ' ')
    f.write(str(math) + ' ')
    f.write(str(avg) + '\n')
'''


while True:
    with open('scorelist.txt', 'a') as f:
        name = input("이름 입력 : ")
        kor = int(input("국어 점수 : "))
        math = int(input("수학 점수 : "))
        avg = (kor + math) / 2
        q = input("성적을 저장할까요?(y/n)")
        if q == 'y':
            f.write(name + ' ')
            f.write(str(kor) + ' ')
            f.write(str(math) + ' ')
            f.write(str(avg) + '\n')
            f.close()
        elif q == 'n':
            f.close()
            print("입력을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

with open('scorelist.txt', 'r') as f:
    data = f.read()
    print("현재 리스트: ")
    print(data)