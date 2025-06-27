import turtle
import time
import random

delay = 0.05

#setting up the screen
w = turtle.Screen()
w.title("Snake Game")
w.bgcolor("#000000")
w.setup(width = 1280, height = 720)
w.tracer(0)

#sprite for food
food = turtle.Turtle()
food.speed(0)
food.color("#0af749")
food.shape("circle")
food.penup()
food.goto(random.randint(-630 , 630), random.randint(-350, 350))

#Sprite for the snake
snake = turtle.Turtle()
snake.speed(0)
snake.color("#ffffff")
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#snake body
body = []

def move_up():
    if snake.direction != "down":
        snake.direction = 'up'

def move_down():
    if snake.direction != "up":
        snake.direction = 'down'

def move_left():
    if snake.direction != "right":
        snake.direction = 'left'

def move_right():
    if snake.direction != "left":
        snake.direction = 'right'

#snake movement
def movement():
    if snake.direction == "up":
        snake.sety(snake.ycor()+20)
    
    if snake.direction == "down":
        snake.sety(snake.ycor()-20)

    if snake.direction == "right":
        snake.setx(snake.xcor()+20)

    if snake.direction == "left": 
        snake.setx(snake.xcor()-20)

#keyboard input
w.listen()
w.onkeypress(move_up, "w")
w.onkeypress(move_down, "s")
w.onkeypress(move_left, "a")
w.onkeypress(move_right, "d")

#ending game
def endgame():
    time.sleep(1)
    snake.goto(0,0)
    snake.direction = "stop"
        
    for b in body:
        b.goto(10000, 10000)
        
    body.clear()

#game loop
while(True):
    w.update()

    #collison with border
    if(snake.xcor()<-630 or snake.xcor()>630 or snake.ycor()>350 or snake.ycor()<-350):
       endgame()

    if snake.distance(food)<20:
        x = random.randint(-630 , 630)
        y = random.randint(-350, 350)
        food.goto(x, y)
        #adding bodies
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("#ffffff")
        new_body.penup()
        body.append(new_body)
    
    #moving the body
    for index in range(len(body)-1, 0 ,-1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)
    
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    movement()

    #body collisons
    for b in body:
        if b.distance(snake) < 20:
            endgame()

    time.sleep(delay)


w.mainloop()
