import csv
import random

def load_questions_from_csv(filename):
    questions = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append({
                'question': row['question'],
                'options': [row['option1'], row['option2'], row['option3'], row['option4']],
                'answer': int(row['answer'])
            })
    return questions

def ask_question(question):
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if answer in [1, 2, 3, 4]:
                return answer == question['answer']
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def run_quiz(questions):
    score = 0
    random.shuffle(questions)  
    for i, question in enumerate(questions):
        if i >= 5:  
            break
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['options'][question['answer'] - 1]}\n")
    
    print(f"Your score for this round is: {score}/{min(len(questions), 5)}")
    return score  

if __name__ == "__main__":
    print("Welcome to the Random Facts Quiz!")
    
    user_name = input("Please enter your name: ")  
    print(f"Hello, {user_name}! Let's get started with the quiz.")
    
    questions = load_questions_from_csv('questions.csv')
    
    total_score = 0  

    while True:  
        round_score = run_quiz(questions)  
        total_score += round_score  

        
        while True:  
            continue_quiz = input("Do you want to continue to the next round? (yes/no): ").strip().lower()
            if continue_quiz in ['yes', 'no']:
                break  
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if continue_quiz == 'no':
            print(f"Thank you for playing, {user_name}! Your total score is: {total_score}.\n")
            break