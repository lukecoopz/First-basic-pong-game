import turtle

# setup screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# scoreboard
score_a = 0
score_b = 0

# create turtles
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()

# bind keys to functions
wn.onkeypress(lambda key: paddle_A(key), "w")  # moves paddle up when 'w' key pressed
wn.onkeypress(lambda key: paddle_A(key), "s")  # moves paddle down when 's' key pressed
wn.onkeypress(lambda key: paddle_B(key), "Up")  # moves paddle down when 'Up' key pressed
wn.onkeypress(lambda key: paddle_B(key), "Down")  # moves paddle up when 'Down' key pressed


# set up paddles
paddle_a.speed(15)  # make the speed of paddle movement constant
paddle_a.shape("square")  # make the shape of paddle a square
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # adjust size of square to make it look like a paddle
paddle_a.color("white")  # colour of paddle is white
paddle_a.penup()  # keep paddle from leaving a trail on the screen when it moves
paddle_a.goto(-350, 0)  # positioning of left-side paddle

paddle_b = turtle.Turtle()
paddle_b.speed(15)  # make the speed of paddle movement constant
paddle_b.shape("square")  # make the shape of paddle a square
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # adjust size of square to make it look like a paddle
paddle_b.color("white")  # colour of paddle is white
paddle_b.penup()  # keep paddle from leaving a trail on the screen when it moves
paddle_b.goto(350, 0)  # positioning of right-side paddle

# set up ball
ball.speed(1)  # make the speed of ball constant
ball.shape("square")  # make the shape of ball a square
ball.shapesize(stretch_wid=1, stretch_len=1)  # adjust size of square to make it look like a ball
ball.color("white")  # colour of ball is white
ball.penup()  # keep ball from leaving a trail on the screen when it moves
ball.goto(0, 0)  # positioning of ball in the center of the screen
ball.dx = 2  # ball speed in x direction
ball.dy = -2  # ball speed in y direction

# collision detection
def ball_collision():
    global score_a, score_b
    if ball.xcor() > 390:  # if the ball hits the right side of the screen
        score_a += 1  # add 1 to score_a
        ball.goto(0, 0)  # reset ball position
        ball.dx *= -1  # change ball direction in x direction
    elif ball.xcor() < -390:  # if the ball hits the left side of the screen
        score_b += 1  # add 1 to score_b
        ball.goto(0, 0)  # reset ball position
        ball.dx *= -1  # change ball direction in x direction
    elif ball.ycor() > 290 or ball.ycor() < -290:  # if the ball hits the top or bottom side of the screen
        ball.dy *= -1  # change ball direction in y direction
    elif (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):  # if the ball hits the right paddle
        ball.dx *= -1  # change ball direction in x direction
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):  # if the ball hits the left paddle
        ball.dx *= -1  # change ball direction in x direction

# function for left-side paddle
def paddle_A(key):
    global score_a
    if key == "w":
        y = paddle_a.ycor()  # get the y coordinate of the paddle
        y += 20  # move the paddle up by increasing its y coordinate
    elif key == "s":
        y = paddle_a.ycor()  # get the y coordinate of the paddle
        y -= 20  # move the paddle down by decreasing its y coordinate
    if y > 290:  # keep the paddle on the screen
        y = 290
    elif y < -290:
        y = -290
    paddle_a.sety(y)  # set the new position of the paddle

# function for right-side paddle
def paddle_B(key):
    global score_b
    if key == "Up":
        y = paddle_b.ycor()  # get the y coordinate of the paddle
        y -= 20  # move the paddle down by decreasing its y coordinate
    elif key == "Down":
        y = paddle_b.ycor()  # get the y coordinate of the paddle
        y += 20  # move the paddle up by increasing its y coordinate
    if y > 290:  # keep the paddle on the screen
        y = 290
    elif y < -290:
        y = -290
    paddle_b.sety(y)  # set the new position of the paddle

# draw border
def draw_border():
    pen = turtle.Turtle()
    pen.speed(0)  # make the drawing speed fast so that it doesn't leave a trail
    pen.color("white")  # the colour of the line is white
    pen.penup()  # don't leave a trail as we move the pen
    for side in range(4):  # we will do this four times to create four sides of the box
        pen.stamp()  # this creates a stamp which is an image of what our turtle looks like at the moment
        angle = 90  # starting angle for each side
        length = 200  # length of each side
        if side == 0 or side == 2:  # if it's the top or bottom side
            pen.forward(length)  # go forward by the length of the side
        else:  # if it's the left or right side
            pen.right(angle)  # turn the turtle to face the next side
            pen.forward(length)  # go forward by the length of the side
            pen.left(180)  # turn the turtle back to face towards the centre

# bind keys to functions
wn.onkeypress(lambda: paddle_A(), "w")  # moves paddle up when 'w' key pressed
wn.onkeypress(lambda: paddle_A(), "s")  # moves paddle down when 's' key pressed
wn.onkeypress(lambda: paddle_B(), "Up")  # moves paddle down when 'Up' key pressed
wn.onkeypress(lambda: paddle_B(), "Down")  # moves paddle up when 'Down' key pressed

wn.ontimer(ball_collision, 10)  # calls the function every 10 milliseconds
wn.ontimer(draw_border, 10)  # calls the function every 10 milliseconds

turtle.done()