import turtle as t  
from turtle import *
import random as r
import time

n = 100.0

speed("fastest") 
screensize(bg='black')  
left(90)
forward(3 * n)
color("orange", "yellow")  
begin_fill()
left(126)
import turtle as t
import random

def draw_star(size):
    t.color("yellow")
    t.begin_fill()

    for _ in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)

    t.end_fill()
t.bgcolor("black")
t.speed(0)

# Vẽ nhiều ngôi sao ngẫu nhiên
for _ in range(100):
    size = random.randint(1, 5)
    x = random.randint(-400, 300)
    y = random.randint(-400, 200)

    t.penup()
    t.goto(x, y)
    t.down()

    draw_star(size)
up()
goto(0,200)
down()
for i in range(5):  
    forward(n / 5)
    right(144)  
    forward(n / 5)
    left(72)  
end_fill()
right(126)

def drawlight():  
    if r.randint(0, 30) == 0:  
        color('tomato')  
        circle(6)  
    elif r.randint(0, 30) == 1:
        color('orange')  
        circle(3)  
    else:
        color('dark green')  


color("dark green")  
backward(n * 4.8)


def tree(d, s): 
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)
def tree1(d, s): 
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .5)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)    
    up()
    goto(0,-275)
    down()
    tree(15,n)
    backward(n/2)
up()
goto(-200, -275)
down()
tree1(15,n)
backward(n/2)
up()
goto(200,-275)
down()
tree1(15,n)
backward(n/2)
for i in range(300):  
    a = 400 - 800 * r.random()
    b = 10 - 30 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)
goto(0,-350)
down()
t.color("dark red", "red") 
t.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))

def drawsnow():  
    t.ht() 
    t.pensize(2) 
    for i in range(100): 
        t.pencolor("white")  
        t.pu() 
        t.setx(r.randint(-350, 350))  
        t.sety(r.randint(-400, 350)) 
        t.pd()  
        dens = 6  
        snowsize = r.randint(1, 10) 
        for j in range(dens): 
           
            t.fd(int(snowsize))
            t.backward(int(snowsize))
           
            t.right(int(360 / dens))  
drawsnow()  

t.done()
