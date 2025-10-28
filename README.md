# Python Snake Game

This is a classic implementation of the Snake Game developed in Python using the standard library module Turtle for graphical rendering.

The goal of the game is to control the snake, consume apples to increase in length and score points, all while avoiding collisions with the boundaries of the game window and the snake's own growing body.

## Features
- Classic Game Logic: Includes core mechanics like snake growth upon eating, border collision detection, and self-collision detection.
- WASD Controls: Intuitive control scheme for movement.
- Real-time Scoreboard: Displays the current score and the snake's size (number of segments) in the game window.
- Quick Restart: Allows the player to restart the game immediately after losing by pressing the Space key.

### Installation

This project utilizes the PythonTurtle library. The necessary dependency is listed in the requirements.txt file.
1. **Clone the repository:**

    ```
    git clone <repository_url>
    cd snake-game-develop
    ```

2. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

### How to play
To start the game, run the main entry point file from your terminal:
`python main.py`

This script initializes the game by creating a Snake instance and calling its on_game() method.

Once the game window appears:
- A welcome message will prompt you to press the Space bar.
- Press Space to begin playing.

### Controls
```
W	    |    Move Up 

S	    |    Move Down

A	    |    Move Left 

D	    |    Move Right

Space	|    Restart the game after the 'You Lose' screen
```
