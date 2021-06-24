#abs(x) 직접 정의
#절대값 알고리즘1
import math

def abs_sign(x):
    if x < 0:
        return -x
    else:
        return x


#절대값2
def abs_square(x):
    y = x*x
    return math.sqrt(y)

print(abs_square(-5))
