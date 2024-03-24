# test_project.py

import pytest
from project import multiply, divide, power, Snake, Food, Scoreboard

# Test cases for custom functions

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(0, 10) == 0
    assert multiply(-2, 8) == -16

def test_divide():
    assert divide(10, 2) == 5
    assert divide(100, 10) == 10
    assert divide(-50, -5) == 10

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, -2) == 0.01


# Test cases for Snake class

def test_snake_initialization():
    snake = Snake()
    assert len(snake.segments) == 3  # Initial length of the snake
    assert snake.head.heading() == 0  # Initial heading of the snake head

def test_snake_move():
    snake = Snake()
    initial_positions = [segment.position() for segment in snake.segments]
    snake.move()
    new_positions = [segment.position() for segment in snake.segments]
    assert new_positions[0] == (20, 0)  # Head moved forward
    assert new_positions[1:] == initial_positions[:-1]  # Rest of the segments follow

def test_snake_extend():
    snake = Snake()
    initial_length = len(snake.segments)
    snake.extend()
    assert len(snake.segments) == initial_length + 1  # Length increased by 1

# Test cases for Food class

def test_food_refresh():
    food = Food()
    initial_position = food.position()
    food.refresh()
    assert food.position() != initial_position  # Position changed after refresh

# Test cases for Scoreboard class

def test_scoreboard_initialization():
    scoreboard = Scoreboard()
    assert scoreboard.score == 0  # Initial score should be 0

def test_scoreboard_increase_score():
    scoreboard = Scoreboard()
    scoreboard.increase_score()
    assert scoreboard.score == 1  # Score increased by 1 after calling increase_score()


# Additional test cases for more coverage can be added similarly

if __name__ == "__main__":
    pytest.main()
