# Level-Based Mini Quiz

# Define questions for each difficulty level
quizzes = {
    "easy": [
        {
            "question": "What color is the sky on a clear day?",
            "options": ["A. Blue", "B. Green", "C. Red", "D. Yellow"],
            "answer": "A"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
            "answer": "B"
        },
        {
            "question": "Which animal says 'meow'?",
            "options": ["A. Dog", "B. Cat", "C. Bird", "D. Cow"],
            "answer": "B"
        },
        {
            "question": "Which day comes after Monday?",
            "options": ["A. Sunday", "B. Tuesday", "C. Wednesday", "D. Friday"],
            "answer": "B"
        },
        {
            "question": "Which shape has 3 sides?",
            "options": ["A. Circle", "B. Triangle", "C. Square", "D. Rectangle"],
            "answer": "B"
        }
    ],
    "medium": [
        {
            "question": "What is the capital of Japan?",
            "options": ["A. Tokyo", "B. Kyoto", "C. Seoul", "D. Beijing"],
            "answer": "A"
        },
        {
            "question": "What is 12 / 4?",
            "options": ["A. 2", "B. 4", "C. 3", "D. 6"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Dickens", "B. Tolkien", "C. Shakespeare", "D. Orwell"],
            "answer": "C"
        },
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "Which gas do plants absorb?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "C"
        }
    ],
    "hard": [
        {
            "question": "What is the square root of 144?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
            "answer": "C"
        },
        {
            "question": "What year did World War II end?",
            "options": ["A. 1942", "B. 1945", "C. 1939", "D. 1950"],
            "answer": "B"
        },
        {
            "question": "Who proposed the theory of relativity?",
            "options": ["A. Newton", "B. Tesla", "C. Einstein", "D. Darwin"],
            "answer": "C"
        },
        {
            "question": "Which element has the chemical symbol 'Au'?",
            "options": ["A. Silver", "B. Oxygen", "C. Gold", "D. Copper"],
            "answer": "C"
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
            "answer": "B"
        }
    ]
}

# Ask the user to select a level
print("Choose a difficulty level:")
print("1. Easy\n2. Medium\n3. Hard")
choice = input("Enter your choice (1/2/3): ").strip()

if choice == "1":
    level = "easy"
elif choice == "2":
    level = "medium"
elif choice == "3":
    level = "hard"
else:
    print("Invalid choice. Defaulting to Easy level.")
    level = "easy"

score = 0
quiz = quizzes[level]

print(f"\nStarting {level.capitalize()} Quiz:")

# Quiz loop
for i, q in enumerate(quiz, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for option in q["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.")

# Final result
print(f"\n🎯 You got {score} out of {len(quiz)} correct in the {level.capitalize()} level.")
