# Snake Game with Turtle Graphics

#### Video Demo:  https://youtu.be/pPQ9h0CpkIg

#### Description:
This project is an implementation of the classic Snake game using Turtle graphics library in Python. The game provides a simple yet engaging gaming experience where players control a snake moving around the screen, eating food to grow longer while avoiding collisions with the walls and its own tail.

### Components:
1. **Snake Class**: Manages the behavior of the snake, including movement, growth, and direction changes. The snake is represented by a series of connected segments.
2. **Food Class**: Represents the food that appears randomly on the screen. When the snake eats the food, it grows longer, and new food spawns at a different location.
3. **Scoreboard Class**: Keeps track of the player's score and displays it on the screen. The score increases each time the snake eats food.
4. **Main Function**: Sets up the game window, initializes the snake, food, and scoreboard, and handles user input for controlling the snake's direction.

### Features:
- **Responsive Controls**: Players can control the snake's direction using arrow keys or other specified keys.
- **Scoring System**: The scoreboard displays the current score, motivating players to achieve higher scores.
- **Game Over Screen**: When the snake collides with the walls or its own tail, the game ends, and a "Game Over" message is displayed.

### Testing:
The project includes comprehensive test cases using the pytest framework to ensure the correctness of the custom functions and classes. Test cases cover various scenarios, including movement, collision detection, and scoring logic.

### How to Run:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `project.py` file using a Python interpreter.
4. Use arrow keys (or specified keys) to control the snake's movement.
5. Enjoy playing the Snake game!

### Future Improvements:
- Implement additional features such as levels, speed increments, or obstacles to enhance gameplay variety.
- Improve the user interface with better graphics and animations.
- Add sound effects and background music to make the game more immersive.

### Credits:
- Turtle Graphics Library: https://docs.python.org/3/library/turtle.html
- Pytest Framework: https://pytest.org/

This project offers a nostalgic gaming experience while also serving as a learning opportunity for Python programming and game development enthusiasts.
