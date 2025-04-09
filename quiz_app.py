def welcome():
    print("Welcome to the Python Quiz!")
    print("Answer the following questions:\n")

def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.strip().lower() == answer.lower()

def run_quiz():
    score = 0
    total_questions = 3

    if ask_question("1. What is the keyword to define a function in Python?", "def"):
        score += 1
    if ask_question("2. What does 'int' stand for in Python?", "integer"):
        score += 1
    if ask_question("3. Which symbol is used for comments in Python?", "#"):
        score += 1

    print(f"\nYou got {score}/{total_questions} correct!")

def main():
    welcome()
    run_quiz()

if __name__ == "__main__":
    main()
