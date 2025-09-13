import turtle
from turtle import *
t=Turtle()

def square(x):
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
  square(200)

def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) 

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()

def rectangle():
   t.forward(125)
   t.left(90)
   t.forward(100)
   t.left(90)
   t.forward(125)
   t.left(90)
   t.forward(100)
   t.left(90)
rectangle()

def equal(x):
   t.forward(x)
   t.left(120)
   t.forward(x)
   t.left(120)
   t.forward(x)
   t.left(120)
equal(90)

#Assesment 1
sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)