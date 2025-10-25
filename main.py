import turtle
import time
import random

class Snake:
    """
    Initialize the Snake Game modules.

    Attributes:
        screen (turtle.Screen): The main game window.
        snake (turtle.Turtle): The turtle object for the snake's head.
        sdata (turtle.Turtle): The turtle object for the scoreboard.
        apples (turtle.Turtle): The turtle object for the food.
        delay (float): The refresh delay for the game loop.
        end_game (bool): Flag to indicate if the game is over.
    """
    def __init__(self):
        """Initializes all the core components required to start a game session."""
        self.screen = turtle.Screen()
        self.snake = turtle.Turtle()
        self.sdata = turtle.Turtle()
        self.apples = turtle.Turtle()
        self.delay = 0.1
        self.end_game = False

        self.screen.setup(width=800, height=800); self.screen.title("Snake Game"); self.screen.bgcolor("#329F5B")
        self.sdata.penup(); self.sdata.speed(0); self.sdata.goto(0, 330); self.sdata.hideturtle()
        self.sdata.color("white"); self.sdata.write("Score: 0 \t\tRecord:0", align="center", font=('Arial', 30, "bold"))
        self.snake.shape("square"); self.snake.penup()
        self.apples.shape("circle"); self.apples.penup(); self.apples.speed(0)
        self.screen.tracer(0)

    #Snake angles direction functions
    def snake_direction_up (self):
        """Sets the snake's heading to Up (90 degrees) if not moving Down."""
        if self.snake.heading() != 270: self.snake.setheading(90)
    def snake_direction_down (self):
        """Sets the snake's heading to Down (270 degrees) if not moving Up"""
        if self.snake.heading() != 90: self.snake.setheading(270)
    def snake_direction_left (self):
        """Sets the snake's heading to Left (180 degrees) if not moving Right."""
        if self.snake.heading() != 0: self.snake.setheading(180)
    def snake_direction_right (self):
        """Sets the snake's heading to Right (0 degrees) if not moving Left."""
        if self.snake.heading() != 180: self.snake.setheading(0)

    #Snake movement function
    def snake_move(self):
        """Activates keyboard listeners and binds keys to movement functions.

            Sets up the game to listen for key presses and maps the WASD Keys to the corresponding snake
            direction methods.
        """
        self.screen.listen() #Listener activation
        self.screen.onkeypress(self.snake_direction_up, "w")
        self.screen.onkeypress(self.snake_direction_down , "s")
        self.screen.onkeypress(self.snake_direction_left , "a")
        self.screen.onkeypress(self.snake_direction_right , "d")

    def border_collision(self):
        """If Snake collides, modifies the end_game value to "True" to end the game."""
        if self.snake.xcor() < -390 or self.snake.xcor() > 390 or self.snake.ycor() < -390 or self.snake.ycor() > 390:
            time.sleep(self.delay)
            self.snake.goto(0,0)
            self.sdata.clear(); self.sdata.goto(0, 50)
            self.sdata.color("red"); self.sdata.write("YOU LOSE\nScore: 0\t\tRecord: 0", align="center", font=('Arial', 30, "bold"));
            self.end_game = True