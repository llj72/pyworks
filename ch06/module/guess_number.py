import random

com = random.randint(1,30)
while True:
    try:
        guess = int(input("맞혀보세요(1~30): "))
        if guess > 30:
            print("숫자 범위를 넘어갔습니다.")
        elif guess < 0:
            print("숫자 범위 이하입니다.")
        else:
            if com > guess:
                print("너무 작아요!")
            elif com < guess:
                print("너무 커요!!")
            elif com == guess:
                print("정답!!")
                break
    except ValueError:
        print("숫자가 아닙니다. 다시 입력해 주세요.")