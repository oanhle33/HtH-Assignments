import turtle
import time
import random

delay=0.1
segments= []
score = 0
high_score = 0

#set up the screen
win =  turtle.Screen()
win.title("My Snake Game")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0)

#create snake's head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "Stop"

#Add some food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# creat pen to write score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "bold"))

def move():
    if head.direction == "up":
        y = head.ycor() # y coodinate of the turle
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor() # y coodinate of the turle
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor() # x coodinate of the turle
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor() # x coodinate of the turle
        head.setx(x-20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"
    
# Main game loop
while True:
    win.update()

    #Check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        score = 0

        #Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segment list
        segments.clear()

    if head.distance(food) < 15:
        #move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #increase the score
        score = score + 10

        if score > high_score:
            high_score = score

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #move the end segment in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)

        #Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

    move()

     # check for head collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # hide the segment
            for segment in segments:
                 segment.goto(1000, 1000)

         # clear segment list
            segments.clear()

    time.sleep(delay)

    #keyboard bindings
    win.listen()
    win.onkey(go_up, "w")
    win.onkey(go_down, "s")
    win.onkey(go_right, "d")
    win.onkey(go_left, "a")

    pen.clear()
    pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "bold"))