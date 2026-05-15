from turtle import *
import turtle as turt
import random
import math


def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
class Bullet(Turtle):
    def __init__(self,player):
        super().__init__()
        self.color(player.color()[0])
        self.hideturtle()
        self.speed(0)
        self.pu()
        self.shape('circle')
        self.shapesize(.2)
        self.setheading(player.heading())
        self.setpos(player.pos())
        self.showturtle()
        self.player = player
    def move(self):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230:
            self.die()
        if self.ycor() > 230 or self.ycor() < -230:
            self.die()


    def die(self):
        self.hideturtle()
        self.player.bullets.remove(self)

class Player(Turtle):
    def __init__(self,x, y, color, screen, right_key, left_key,fire_key):
        super().__init__()
        self.ht()
        self.health = 3
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        self.lflag=False
        self.rflag=False
        screen.onkeypress(self.setl, left_key)
        screen.onkey(self.unsetl, left_key)
        screen.onkeypress(self.setr, right_key)
        screen.onkey(self.unsetr, right_key)
        screen.onkey(self.fire,fire_key)
    def unsetl(self):
        self.lflag=False
    def setl(self):
        self.lflag=True
    def setr(self):
        self.rflag=True
    def unsetr(self):
        self.rflag=False
    def move_(self):
        self.forward(4)
        if self.lflag:
            self.left(10)
        if self.rflag:
            self.right(10)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())
   
    def fire(self):
        self.bullets.append(Bullet(self))

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

playing_area()
bullets=[]
p1 = Player(-100, 0, "#FF0000",screen, "d", "a","w")
p2 = Player(100,0,"#0000FF",screen, "Right","Left","Up")


while p1.alive ==True and p2.alive == True:
    p1.move_()
    p2.move_()
   
    for i in p1.bullets:
        i.move()
        if i.distance(p2) < 20:
            i.die()
            p2.health -=1
            if p2.health == 2:
                p2.color("#000088")
            elif p2.health == 1:
                p2.color("#000044")
            else:
                p2.hideturtle()
                p2.alive == False
    for i in p2.bullets:
        i.move()
        if i.distance(p1) < 20:
            i.die()
            p1.health -=1
            if p1.health == 2:
                p1.color("#880000")
            elif p1.health == 1:
                p1.color("#440000")
            else:
                p1.hideturtle()
                p1.alive == False


                p1.hideturtle()

screen.exitonclick()
