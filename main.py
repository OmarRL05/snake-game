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
        apple (turtle.Turtle): The turtle object for the food.
        delay (float): The refresh delay for the game loop.
        end_game (bool): Flag to indicate if the game is over.
        apple_points (int): The apples score of the game.
        snake_size (int): Indicate the snake size on the game.
        snake_body (list): Contains turtle objects for the snake's body.
    """
    def __init__(self):
        """Initializes all the core components required to start a game session."""
        self.screen = turtle.Screen(); self.screen.listen() #Listener activation
        self.snake = turtle.Turtle()
        self.sdata = turtle.Turtle()
        self.lose = turtle.Turtle()
        self.apple = turtle.Turtle()
        self.delay = 0.1
        self.apple_points, self.snake_size = 0, 0
        self.end_game = False
        self.press_x = False
        self.snake_body = []

        self.screen.setup(width=800, height=800); self.screen.title("Snake Game"); self.screen.bgcolor("#329F5B")
        self.sdata.penup(); self.sdata.speed(0); self.sdata.goto(0, 330); self.sdata.hideturtle()
        self.sdata.color("white"); self.sdata.write(f"Score: {self.apple_points} \tSize: {self.snake_size}", align="center", font=('Arial', 30, "bold"))
        self.lose.hideturtle(); self.lose.penup(); self.lose.color("red"); self.lose.speed(0); self.lose.goto(0, 20)
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
        self.screen.onkeypress(self.snake_direction_up, "w")
        self.screen.onkeypress(self.snake_direction_down , "s")
        self.screen.onkeypress(self.snake_direction_left , "a")
        self.screen.onkeypress(self.snake_direction_right , "d")

    def snake_body_move(self):
        """Tracks snake's head position and moves its body along its direction"""
        if self.snake_body != []:
            for i in range(len(self.snake_body) - 1, 0, -1):
                self.snake_body[i].goto(self.snake_body[i - 1].pos())
            self.snake_body[0].goto(self.snake.position())

    def snake_grow(self):
        """Creates and adds a new segment to the snake's body.

            Each new segment is initialized as a Turtle object, styled, and appended
            to the `snake_body` list.
        """
        snake_chest = turtle.Turtle()
        snake_chest.shape("square")
        snake_chest.penup()
        snake_chest.color("green")
        snake_chest.speed(0)
        snake_chest.goto(410, 410)
        self.snake_body.append(snake_chest)

    def snake_collision(self):
        """Checks for collision between the snake's head and its own body

            Iterates through each segment of the snake's body (excluding the
            segment right behind the head) and sets the `end_game` flag to True
            if the head gets too close to any part of its body.
        """
        for chest in self.snake_body[1:]:
            if self.snake.distance(chest) < 10:
                self.lose_screen()

    def border_collision(self):
        """If Snake collides, modifies the end_game value to "True" to end the game."""
        if self.snake.xcor() < -390 or self.snake.xcor() > 390 or self.snake.ycor() < -390 or self.snake.ycor() > 390:
            self.lose_screen()

    def apple_collision(self):
        """Checks for collision with the apple and updates the game state.

            If the snake's head is close enough to the apple, this method
            triggers the following events:
            - The apple is moved to a new random location.
            - The player's score and snake's size are incremented.
            - The on-screen scoreboard is updated to reflect the new values.
            """
        if self.snake.distance(self.apple) < 20:
            self.snake_grow()
            self.apple_points += 10
            self.snake_size += 1
            self.apple.goto(random.randint(-390, 390), random.randint(-390, 390))
            self.sdata.clear()
            self.sdata.write(f"Score: {self.apple_points} \tSize: {self.snake_size}", align="center", font=('Arial', 30, "bold"))

    def lose_screen(self):
        time.sleep(self.delay)
        self.snake.goto(0, 0)
        self.lose.write("\tYou Lose\n Press Space to Play again", align="center", font=('Arial', 40, "bold"))
        for chest in self.snake_body:
            chest.hideturtle()
        self.snake_body.clear()
        self.apple_points, self.snake_size = 0, 0
        self.end_game = True
        self.screen.update()

    def start_snake(self):
        """Starts user's gameplay and updates screen information """
        time.sleep(1)
        self.snake_move()
        self.lose.clear()
        self.screen.update() #Clear screen before start playing
        while not self.end_game:
            self.snake_body_move()
            self.snake.forward(20)
            self.border_collision()
            self.apple_collision()
            self.screen.update()
            time.sleep(self.delay)
        self.end_game = False

    def menu_keys(self):
        self.screen.onkeypress(self.start_snake, "space")

    def on_game(self):

        """Main function

            Allows to restart once a game ends. Restarts the snake size, respawns the apple again and cleans the
            full snake's body.
        """
        #Welcome screen
        welcome_text = turtle.Turtle()
        welcome_text.hideturtle()
        welcome_text.penup()
        welcome_text.sety(-50)
        welcome_text.color("white")
        welcome_text.write("Press 'space' to start", align="center", font=('Arial', 25, "normal"))
        self.screen.update()
        time.sleep(3)
        welcome_text.clear()
        self.screen.update()
        #Reading `Space` to play again
        self.menu_keys()
        #Screen updates ending
        self.screen.mainloop()

Snake_game = Snake()
Snake_game.on_game()