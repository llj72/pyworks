
def vartest():
    global a
    a = a +1  # a : 지역변수
    return a
    
a = 1 #전역 변수
print(vartest())
print(a)
