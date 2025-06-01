# Rock-Paper-Scissors Game

## Overview
A simple Python implementation of the classic Rock-Paper-Scissors game where you play against the computer in a best-of-3 match.

## Features
- Player vs Computer gameplay
- Score tracking across multiple rounds
- Input validation to ensure proper choices
- Clear winner determination after 3 rounds
- Simple and intuitive command-line interface

## How to Play
1. Run the Python script
2. When prompted, enter your choice: "rock", "paper", or "scissors"
3. The computer will randomly select its choice
4. The winner of each round is determined based on standard Rock-Paper-Scissors rules:
   - Rock beats Scissors
   - Scissors beat Paper
   - Paper beats Rock
5. The game plays 3 rounds and declares an overall winner

## Code Structure
The program consists of several key functions:

1. `get_user_choice()` - Handles user input with validation
2. `get_computer_choice()` - Generates random computer choice
3. `determine_winner()` - Compares choices and updates scores
4. `overall_winner()` - Determines the final winner after 3 rounds

## Requirements
- Python 3.x
- random module (included in Python standard library)

## How to Run
1. Save the code to a file (e.g., `rock_paper_scissors.py`)
2. Open a terminal/command prompt
3. Navigate to the directory containing the file
4. Run the command: `python rock_paper_scissors.py`

## Sample Output
Let's play Rock, Paper, Scissors!
This game is the best of 3!

Round: 1
Enter your choice (rock, paper, or scissors): rock
You chose: rock
Computer chose: scissors
Congratulations! You win this round!

Round: 2
Enter your choice (rock, paper, or scissors): paper
You chose: paper
Computer chose: scissors
Computer wins this round!

Round: 3
Enter your choice (rock, paper, or scissors): paper
You chose: paper
Computer chose: rock
Congratulations! You win this round!

You won the overall match
---

## Future Enhancements
- Add option to play more or fewer rounds
- Implement a graphical user interface
- Add game statistics tracking
- Include additional game variations (e.g., Rock-Paper-Scissors-Lizard-Spock)

## Author
Golla Bhargava Teja

## License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
