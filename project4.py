def run_quiz():
    """Ask the user general knowledge questions and track the score."""

    questions = [
        {
            "question": "What is the capital of France?",
            "answer": "paris"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "jupiter"
        },
        {
            "question": "How many continents are there on Earth?",
            "answer": "7"
        }
    ]

    score = 0

    print("Welcome to the General Knowledge Quiz!\n")

    for i, q in enumerate(questions, start=1):
        user_answer = input(f"Q{i}: {q['question']} ").strip().lower()

        if user_answer == q["answer"]:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was: {q['answer'].title()}\n")

    print("-----------------------------")
    print(f"Quiz complete! Your final score is {score}/{len(questions)}")
    print("-----------------------------")


if __name__ == "__main__":
    run_quiz()