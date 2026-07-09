# General Knowledge Quiz

A simple Python command-line quiz game that asks the user 3 general knowledge questions, keeps score, and prints the final result at the end.

## Features

- Asks 3 general knowledge questions (e.g., "What is the capital of France?")
- Tracks the user's score, awarding +1 point for every correct answer
- Case-insensitive answer checking
- Prints the final score at the end of the quiz

## Requirements

- Python 3.6+

No external dependencies — built entirely with core Python.

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/laxmipriyaksheersagar/project-quiz-.git
cd general-knowledge-quiz
python general_knowledge_quiz.py
```

You'll be asked each question in turn and told immediately whether your answer was correct:

```
Welcome to the General Knowledge Quiz!

Q1: What is the capital of France? paris
Correct! ✅

Q2: What is the largest planet in our solar system? mars
Wrong! ❌ The correct answer was: Jupiter

Q3: How many continents are there on Earth? 7
Correct! ✅

-----------------------------
Quiz complete! Your final score is 2/3
-----------------------------
```

## How It Works

1. Questions and their correct answers are stored as a list of dictionaries.
2. The script loops through each question, prompts the user, and compares their (lowercased, trimmed) input to the correct answer.
3. A `score` variable increments for every correct answer.
4. This demonstrates **control flow** — using `if/else` logic and variables to direct the program based on user input.

## Key Skill Demonstrated

- **If-Else Logic & Variables**: This project teaches how to direct a program's behavior based on user choices, a foundational concept in programming.

## Possible Enhancements

- Add more questions or load them from a file (JSON/CSV)
- Randomize question order
- Add multiple-choice options instead of free text
- Add a timer for each question
- Handle minor typos or punctuation in answers

## License

This project is licensed under the MIT License. Feel free to use and modify it as you like.
