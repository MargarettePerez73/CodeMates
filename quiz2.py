import csv
import random
import time

def display_welcome():
    print("\n" + "=" * 70)
    print("🌟✨ WELCOME TO THE ULTIMATE QUIZ GAME!✨🌟".center(70))
    print("=" * 70)
    time.sleep(1)

def display_separator(title):
    print("\n" + "=" * 70)
    print(f"✨ {title} ✨".center(70))
    print("=" * 70)

def load_questions_from_csv(filename):
    questions = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append({
                    'question': row['question'],
                    'options': [row['option1'], row['option2'], row['option3'], row['option4']],
                    'answer': int(row['answer'])
                })
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return []
    except KeyError as e:
        print(f"❌ Error: Missing column in CSV file: {e}")
        return []
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return []
    return questions

def ask_question(question):
    display_separator("QUIZ TIME")
    print(question['question'].center(70))
    print("\n" + "=" * 70)
    for i, option in enumerate(question['options']):
        print(f"{i + 1}. {option}".center(70))
    print("=" * 70)
    while True:
        try:
            answer = int(input("\n✨ Your answer (1-4): ").strip())
            if answer in range(1, 5):
                return answer == question['answer']
            else:
                print("❌ Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    total_questions = min(len(questions), 5)
    for i in range(total_questions):
        correct = ask_question(questions[i])
        if correct:
            print("\n🎉 Correct! Well done! 🎉\n".center(70))
            score += 1
        else:
            correct_answer = questions[i]['options'][questions[i]['answer'] - 1]
            print(f"\n❌ Wrong! The correct answer was: {correct_answer} ❌\n".center(70))
        time.sleep(1)
    display_separator("SCORE REPORT")
    print(f"Your score: {score}/{total_questions}".center(70))
    return score

if __name__ == "__main__":
    display_welcome()
    user_name = input("✨ Please enter your name: ").strip()
    print(f"\nHello, {user_name}! Get ready for an amazing quiz experience!\n".center(70))
    time.sleep(1)

    questions = load_questions_from_csv('questions2.csv')
    if not questions:
        print("No questions available. Exiting the quiz.".center(70))
        exit()

    total_score = 0
    while True:
        round_score = run_quiz(questions)
        total_score += round_score
        print("\n" + "=" * 70)
        continue_quiz = input("🔄 Do you want to play another round? (yes/no): ").strip().lower()
        print("=" * 70)
        if continue_quiz == 'no':
            display_separator("THANK YOU FOR PLAYING")
            print(f"✨ Your total score: {total_score} ✨".center(70))
            print("\nGoodbye, and see you next time!".center(70))
            break
