import turtle
import time
import random

delay = 0.1

# Game Window
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("lime")
wn.setup(width=600, height=600)
wn.tracer(0)

# Head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Yılan yiyeceğini oluşturma
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []


def goUp():
    if head.direction != "down":
        head.direction = "up"


def goDown():
    if head.direction != "up":
        head.direction = "down"


def goRight():
    if head.direction != "left":
        head.direction = "right"


def goLeft():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Keyboard Controls
wn.listen()
wn.onkeypress(goUp, "w")
wn.onkeypress(goDown, "s")
wn.onkeypress(goLeft, "a")
wn.onkeypress(goRight, "d")

while True:
    wn.update()

    # Sınırlar kontrolü
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        # Yemek yeme kontrolü
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Segment hareketi
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Kuyruk ve baş çarpışması kontrolü
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)

wn.mainloop()
