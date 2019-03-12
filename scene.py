import turtle
chad = turtle
import random

user_rating = int(input("How many stars do you want yeeted?: "))

chad.speed(0)

def draw_space():
    for i in range(2):
        chad.forward(1000)
        chad.left(90)
        chad.forward(500)
        chad.left(90)

def draw_earth():
    chad.color("green")
    chad.setposition(0,-1700)
    chad.pendown()
    chad.begin_fill()
    chad.circle(800)
    '''chad.left(130)
    chad.pendown()
    chad.begin_fill()
    chad.circle(300,90)'''
    chad.end_fill()
   
#Sunset
def draw_sunset():
    radius = 20
    for i in range(50):
        if(i > 0):
            chad.pendown()
            chad.circle(radius,360,i)
        else:
            chad.penup()
            chad.setposition(-200,-200)
            chad.setposition(0,0)
            chad.pendown()
        chad.penup()
        chad.setposition(0,-250)
        radius += 20

#Draws white border
def border():
    chad.pensize(300)
    chad.color("white")
    chad.setposition(-650,-350)
    chad.pendown()
    chad.left(90)
    chad.forward(750)
    chad.right(90)
    chad.forward(1300)
    chad.right(90)
    chad.forward(800)
    chad.right(90)
    chad.forward(1300)
    chad.penup()

#Star function
def stars():
    for i in range(5):
        chad.forward(20)
        chad.right(144)
    
#Draw stars
def draw_stars():
    for x in range(user_rating):
        chad.setposition(random.randint(-500,500),random.randint(100,250))
        chad.pendown()
        stars()
        chad.penup()

#Draws planet
def planet():
    chad.setposition(350,100)
    chad.color("#ff6666")
    chad.begin_fill()
    chad.circle(40)
    chad.end_fill()

#Draws moon
def moon():
    chad.setposition(400,150)
    chad.color("#b3b3b3")
    chad.begin_fill()
    chad.circle(10)
    chad.end_fill()

#Draws crater
def crater():
    chad.setposition(395,155)
    chad.color("#7b8799")
    chad.begin_fill()
    chad.circle(3)
    chad.end_fill()
    #chad.color("#4f5763")
    #chad.circle(3)
    chad.setposition(405,160)
    chad.color("#7b8799")
    chad.begin_fill()
    chad.circle(2)
    chad.end_fill()
    #chad.setposition(405,160)
    #chad.color("#4f5763")
    #chad.circle(2)

#Everything together
for i in range(1):
    chad.penup()
    chad.setposition(-500,-250)
    #hungry = random.randint(0,1)
    hungry = 0
    chad.pendown()
    if(hungry == 0):
        chad.color("#66ccff")
        chad.begin_fill()
        draw_space()
        chad.end_fill()
        chad.color("white")
        chad.pensize(5)
        chad.penup()
        draw_stars()
        chad.pensize(2)
        chad.color("orange")
        draw_sunset()
        draw_earth()
        chad.penup()
    else:
        chad.color("black")
        chad.begin_fill()
        draw_space()
        chad.end_fill()
        chad.color("white")
        chad.pensize(5)
        chad.penup()
        draw_stars()
        chad.pensize(1)
        planet()
        moon()
        crater()
        chad.penup()
        draw_earth()
    border()
      
