def ask_question(question, answer, choices):
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    
    user_answer = input("Enter the number of your answer: ")
    
    if choices[int(user_answer) - 1] == answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was: {answer}\n")
        return False

def quiz():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris", "choices": ["Berlin", "Madrid", "Paris", "Rome"]},
        {"question": "What is 2 + 2?", "answer": "4", "choices": ["3", "4", "5", "6"]},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars", "choices": ["Earth", "Mars", "Jupiter", "Venus"]}
    ]
    
    score = 0
    for q in questions:
        if ask_question(q["question"], q["answer"], q["choices"]):
            score += 1
    
    print(f"Your final score is: {score}/{len(questions)}")

# Run the quiz
quiz()
