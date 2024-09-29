import turtle
import time
import random

SNAKE_SPEED = 0.15
SNAKE_STEP = 23
SNAKE_COLOR = "brown"
SNAKE_COLOR2 = "orange"
SCREEN_X = 400
SCREEN_Y = 400
BABY_SNAKE = 3
SNAKE_FAT = 10


direction = ('right','left',"up","down")
snake = []
direction = "right"
bRunning = True
iPoints = -10
iExtraPoints = 0


screen = turtle.Screen()
screen.setup(SCREEN_X*2,SCREEN_Y*2)
screen.bgpic("background.jpg")
screen.addshape("apple.png")
screen.addshape("rotten_apple.png")


food = turtle.Turtle()
food.shape("apple.png")
food.speed(0)
food.hideturtle()
food.setheading(90)


badFood = food.clone()
badFood.shape("rotten_apple.png")



points = turtle.Turtle()
points.color("white")
points.speed(0)
points.pu()
points.goto(-SCREEN_X+16,SCREEN_Y-28)
points.pd()


rect = turtle.Turtle()
rect.color("blue")
rect.speed(0)
rect.pu()
rect.setpos(-SCREEN_X+10,SCREEN_X-10)
rect.pd()
for x in range(4):
  rect.forward(SCREEN_X*2-20)
  rect.right(90)
rect.ht()

snakePiece = turtle.Turtle()
lastColor = SNAKE_COLOR
snakePiece.color(lastColor)
snakePiece.shape("square")
snakePiece.speed(0)
snakePiece.penup()
snakePiece.hideturtle()
snakePiece.goto(-SCREEN_X,0)
snakePiece.pendown()
snakePiece.showturtle()
snake.append(snakePiece)