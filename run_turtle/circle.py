#여러 개의 원 만들기
import turtle as t

t.speed(5) #speed 1 ~9, 0이 가장 빠
t.color('green')
n = 50
for x in range(n):
    t.circle(80)
    t.left(360/n)
