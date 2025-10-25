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
        apple_points (int): The apples score of the game
        snake_size (int): Indicate the snake size on the game
    """
    def __init__(self):
        """Initializes all the core components required to start a game session."""
        self.screen = turtle.Screen()
        self.snake = turtle.Turtle()
        self.sdata = turtle.Turtle()
        self.apple = turtle.Turtle()
        self.delay = 0.1
        self.end_game = False
        self.apple_points, self.snake_size = 0, 0

        self.screen.setup(width=800, height=800); self.screen.title("Snake Game"); self.screen.bgcolor("#329F5B")
        self.sdata.penup(); self.sdata.speed(0); self.sdata.goto(0, 330); self.sdata.hideturtle()
        self.sdata.color("white"); self.sdata.write(f"Score: {self.apple_points} \tSize: {self.snake_size}", align="center", font=('Arial', 30, "bold"))
        self.snake.shape("square"); self.snake.penup()
        self.apple.shape("circle"); self.apple.penup(); self.apple.speed(0); self.apple.color("red")
        self.apple.goto(random.randint(-390, 390), random.randint(-390, 390))
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

    def apple_collision(self):
        """Checks for collision with the apple and updates the game state.

            If the snake's head is close enough to the apple, this method
            triggers the following events:
            - The apple is moved to a new random location.
            - The player's score and snake's size are incremented.
            - The on-screen scoreboard is updated to reflect the new values.
            """
        if self.snake.distance(self.apple) < 20:
            self.apple_points += 10
            self.snake_size += 1
            self.apple.goto(random.randint(-390, 390), random.randint(-390, 390))
            self.sdata.clear();
            self.sdata.write(f"Score: {self.apple_points} \tSize: {self.snake_size}", align="center", font=('Arial', 30, "bold"))
            self.screen.update()
            time.sleep(self.delay)

    def start_snake(self):
        """Starts user's gameplay and updates screen information """
        while not self.end_game:
            self.snake.forward(20)
            self.border_collision()
            self.apple_collision()
            self.screen.update()
            time.sleep(self.delay)
        self.screen.mainloop()