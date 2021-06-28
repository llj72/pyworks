#1번
def is_odd(number):
    if number % 2 == 1 :
        return True
    else:
        return False
print(is_odd(5))
print(is_odd(6))

#2번
#가변 매개변수
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2))

#3번
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

#4번
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))