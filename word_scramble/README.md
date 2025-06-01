# Word Scramble Game 

A fun Python-based word scramble game that challenges players to unscramble words with limited attempts.

## Features 
-  Random word scrambling from a predefined list
-  Limited attempts (3 tries per word)
-  Option to play multiple rounds
-  Clean exit functionality
-  Immediate feedback on guesses
-  Expandable word list

## Requirements 
- Python IDE
- No external dependencies required

## Installation & Usage 

1. **Download the script**:
   ```bash
   wget https://raw.githubusercontent.com/bhargavatejagolla/word-scramble-game/main/word_scramble.py
   ```
2. **Run the game**: python word_scramble.py
3. ### Gameplay Instructions:

- You'll see a scrambled word  
- Type your guess to unscramble it  
- You get **3 attempts** per word  
- Type `'exit'` anytime to quit  
- After each word, choose to **play again** or **quit**
4. ### How It Works 

- Selects a random word from the predefined list  
- Scrambles the letters using the **Fisher-Yates algorithm**  
- Presents the scrambled word to the player  
- Validates guesses against the original word  
- Provides attempt tracking and feedback  
- Offers continuous play until the player exits
## Word List 📝

The game currently includes these words:

`python`, `developer`, `programming`, `algorithm`, `function`  
`variable`, `debugging`, `compiler`, `codechef`, `machine`  
`bitcoin`, `operation`
  
## Example Gameplay
<pre>
Welcome to the Word Scramble Game!
Scrambled word: lpphyo

Guess the word (or type 'exit' to quit): python
Correct! You guessed it!
The correct word was: python

Do you want to play again? (yes/no): yes
Welcome to the Word Scramble Game! 
Scrambled word: vgindebgu
Guess the word (or type 'exit' to quit): debug 
Wrong guess. Attempts left: 2 

Guess the word (or type 'exit' to quit): debugging
Correct! You guessed it!
The correct word was: debugging
</pre>
## Customization 🛠️

- **Expand word list**: Add more words to the `word_list`
- **Difficulty settings**: Modify the `attempts` variable
- **Scrambling intensity**: Adjust the `scramble_word()` function
- **Add hints**: Implement a hint system after failed attempts

---
## Contributing 

Contributions welcome! Ideas to enhance the game:

- Add difficulty levels
- Implement a scoring system
- Create word categories (e.g., tech, animals, etc.)
- Add a timer for speed rounds

---

## License 📄

**MIT License** – Free to use, modify, and share.

