# 전역 변수의 범위

def price():
    price = 250 * quantity
    print("{}원입니다.".format(price))

quantity = 2
print("{}개에".format(quantity))
price()
