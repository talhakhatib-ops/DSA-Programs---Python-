# Program to run a simple multiple-choice quiz

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. fun"],
        "answer": "B"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "What is the result of 10 // 3 in Python?",
        "options": ["A. 3.33", "B. 1", "C. 4", "D. 3"],
        "answer": "D"
    },
    {
        "question": "Which loop repeats while a condition is true?",
        "options": ["A. for", "B. while", "C. if", "D. switch"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    }
]

score = 0

print("===== Python Multiple-Choice Quiz =====")

for number, item in enumerate(questions, start=1):
    print(f"\nQ{number}. {item['question']}")

    for option in item["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", item["answer"])

print("\n===== Quiz Result =====")
print(f"Your score: {score}/{len(questions)}")
print(f"Percentage: {score / len(questions) * 100:.1f}%")
