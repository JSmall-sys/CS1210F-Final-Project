import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("THE MAZE GAME")

# create turtle 2
egbert = turtle.Turtle()
egbert.shape("turtle")
egbert.color("green")
egbert.penup()

# create end turtle
endt = turtle.Turtle()
endt.shape("turtle")
endt.color("red")
endt.penup()

# create wall-drawing turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()

# Wall Cordinates
walls = [
#Horizontal Walls
    (-200, 200, 0, 200), #Top Horizontal Wall
    (-200, -200, 0, -200), #Bottom Horizontal Wall
    (-200, -80, -160, -80),
    (-200, 40, -120, 40),
    (-200, 160, -160, 160),
    (-160, -160, -120, -160),
    (-160, -120, -120, -120),
    (-160, -40, -80, -40),
    (-160, 0, -80, 0),
    (-160,80, -80, 80),
    (-80, 40, -40, 40),
    (-80, 160, 0, 160),
    (-40, -80, 0, -80),
    (-40, 40, 0, 40),
#Vertical Walls
    (-200, 200, -200, -200), #Left Vertical Wall
    (0, 200, 0, -200), #Right Vertical Wall
    (-160, -200, -160, -120),
    (-160, -40, -160, 0),
    (-160, 120, -160, 160),
    (-120, -120, -120, -80),
    (-120, 80, -120, 200),
    (-80, -160, -80, -40),
    (-80, 80, -80, 120),
    (-40, -160, -40, -80),
    (-40, -40, -40, 40),
    (-40, 120, -40, 160)
]

def wall_collision(x, y):
    radius = 5
    for x1, y1, x2, y2 in walls:
        if x1 == x2:  # vertical wall
            if min(y1, y2) - radius <= y <= max(y1, y2) + radius and abs(x - x1) <= radius:
                return True
        elif y1 == y2:  # horizontal wall
            if min(x1, x2) - radius <= x <= max(x1, x2) + radius and abs(y - y1) <= radius:
                return True
    return False

# draws walls
def draw_wall(x1, y1, x2, y2):
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()

for wall in walls:
    draw_wall(*wall)

# movement keys
keys = [False, False, False, False]


def on_press_up():
    keys[0] = True
def on_release_up():
    keys[0] = False
def on_press_down():
    keys[1] = True
def on_release_down():
    keys[1] = False
def on_press_left():
    keys[2] = True
def on_release_left():
    keys[2] = False
def on_press_right():
    keys[3] = True
def on_release_right():
    keys[3] = False

def movement(time_step):
    speed = 75
    original_pos = egbert.pos()
    
    if keys[0]:
        egbert.setheading(90)
        egbert.forward(speed * time_step)
    if keys[1]:
        egbert.setheading(270)
        egbert.forward(speed * time_step)
    if keys[2]:
        egbert.setheading(180)
        egbert.forward(speed * time_step)
    if keys[3]:
        egbert.setheading(0)
        egbert.forward(speed * time_step)

    x, y = egbert.pos()

    if not (-200 <= x <= 200 and -200 <= y <= 200) or wall_collision(x, y):
        egbert.setposition(start_pos)
    
#Starting points
start=random.randint(1, 4)
end=random.randint(1, 4)
while start == end:
    end=random.randint(1, 4)
    
if start == 1:
    start_pos = (-100, 90)
elif start == 2:
    start_pos = (-190, -190)
elif start == 3:
    start_pos = (-20, 190)
else:
    start_pos = (-20, -90)

egbert.setposition(start_pos)

#Endpoints
if end == 1:
    end_pos = (-100, 90)
elif end == 2:
    end_pos = (-190, -190)
elif end == 3:
    end_pos = (-20, 190)
else:
    end_pos = (-20, -90)
    
endt.setposition(end_pos)

previous = time.time()

# game loop
def game_loop():
    global previous
    current = time.time()
    time_step = current - previous
    previous = current

    movement(time_step)

    if abs(egbert.xcor() - endt.xcor()) <= 5 and abs(egbert.ycor() - endt.ycor()) <= 5:
        print("You win!")
        
    else:
        screen.ontimer(game_loop, 16)

screen.onkeypress(on_press_up, "Up")
screen.onkeyrelease(on_release_up, "Up")
screen.onkeypress(on_press_down, "Down")
screen.onkeyrelease(on_release_down, "Down")
screen.onkeypress(on_press_left, "Left")
screen.onkeyrelease(on_release_left, "Left")
screen.onkeypress(on_press_right, "Right")
screen.onkeyrelease(on_release_right, "Right")
screen.listen()

game_loop()
screen.mainloop()
