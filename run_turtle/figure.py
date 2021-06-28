#도형 그리기

import turtle as t

t.shape("turtle")

#사각형 그리기
i = 1
n =4
while i <=4:
    t.forward(100)
    t.right(360/n)
    i +=1

#삼각형 그리기
t.color('red')
t.pensize(2)
i = 1
n=3
while i <=3:
    t.forward(100)
    t.right(360/n)
    i +=1

# 원
t.color('blue')
t.pensize(3)
t.circle(50)

t.mainloop()