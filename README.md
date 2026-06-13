# 21 Number Game (User vs Computer)

## Description

This is a simple Python implementation of the classic 21 Number Game. The player competes against the computer by taking turns saying consecutive numbers. On each turn, a player may say 1, 2, or 3 numbers. The player who is forced to say 21 loses the game.

The project was created to practice Python fundamentals such as loops, conditionals, user input, functions, and random number generation.

## Features

  - User vs Computer gameplay
  - Random computer moves
  - Input validation for numbers 1–3
  - Automatic tracking of the current number
  - Win/Loss detection

## How to Play

1. Run the program.
2. Enter how many consecutive numbers you want to say (1–3).
3. The program will display the numbers you said.
4. The computer will randomly choose and display its numbers.
5. Players continue taking turns until someone reaches 21.
6. The player who says 21 loses.

## Example Gameplay

How many numbers do you want to say? (1-3): 3

You:
1
2
3

Computer chooses 2 number(s):
4
5

How many numbers do you want to say? (1-3): 3

You:
6
7
8

...

How many numbers do you want to say? (1-3): 2

You:
19
20

Computer chooses 3 number(s):
21
Computer said 21. Computer loses!

### Note

This project intentionally uses a command-line interface (CLI) instead of a graphical user interface (GUI). The goal was to focus on learning and practicing fundamental Python concepts such as loops, conditionals, functions, input handling, and game logic.
