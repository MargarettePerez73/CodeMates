import csv
import random
import tkinter as tk
from tkinter import messagebox
import os
from PIL import ImageTk, Image

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiztopia")
        self.master.geometry("1760x990")

        self.bg_image = Image.open(r'C:\Users\Huawei Matebook\Desktop\PythonTest\1.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        

        self.bg_label = tk.Label(master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.player_name = ""
        self.total_score = 0
        self.current_question_index = 0
        self.questions = []
        self.timer = 30
        self.timer_running = False

        self.title_label = tk.Label(master, text="\n🌟✨ WELCOME TO QUIZTOPIA!✨🌟\n", font=("pixelmix", 40), fg="#ffffff", bg="#000000")
        self.title_label.pack(pady=20)

        self.name_label = tk.Label(master, text="Please enter your name:", font=("pixelmix", 30), fg="#00FF00", bg="#000000")
        self.name_label.pack()
        self.name_entry = tk.Entry(master, font=("pixelmix", 30))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Quiz", font=("pixelmix", 20), fg="#ffffff", bg="#D10000", command=self.choose_quiz)
        self.start_button.pack(pady=20)

        self.question_frame = None
        self.question_label = None
        self.options_var = None
        self.options = []
        self.submit_button = None
        self.timer_label = None

        self.leaderboard = []
        self.load_leaderboard()

    def choose_quiz(self):
        self.player_name = self.name_entry.get() or "Player"
    
        if self.is_name_taken(self.player_name):
            messagebox.showerror("Name Taken", "This name has already been used. Please choose another one.")
            return
    
        for widget in self.master.winfo_children():
            if widget not in [self.bg_label]:
                widget.destroy()
    
        self.quiz_label = tk.Label(self.master, text=f"Hello {self.player_name}, choose your quiz:", font=("pixelmix", 40), fg="#ffffff", bg="#000000")
        self.quiz_label.pack(pady=20)

        self.programming_button = tk.Button(self.master, text="Programming", fg="#ffffff", bg="#00C0CE", command=lambda: self.start_quiz('questions2.csv'), font=("pixelmix", 30))
        self.programming_button.pack(pady=10)

        self.random_facts_button = tk.Button(self.master, text="Random Facts", fg="#ffffff", bg="#33CE00", command=lambda: self.start_quiz('questions.csv'), font=("pixelmix", 30))
        self.random_facts_button.pack(pady=10)

    def start_quiz(self, filename):
        self.load_questions_from_csv(filename)
        self.questions = random.sample(self.questions, min(10, len(self.questions)))
        self.current_question_index = 0
        self.total_score = 0
        self.show_question()

    def load_questions_from_csv(self, filename):
        self.questions = []
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.questions.append({
                        'question': row['question'],
                        'options': [row['option1'], row['option2'], row['option3'], row['option4']],
                        'answer': int(row['answer'])
                    })
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{filename}' was not found.")

    def show_question(self):
     if self.current_question_index < len(self.questions):
        self.clear_quiz_selection()
        question = self.questions[self.current_question_index]

        self.bg_image = Image.open(r'C:\Users\Huawei Matebook\Desktop\PythonTest\2.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo

        self.question_label = tk.Label(self.master, text=question['question'], wraplength=700, font=('pixelmix', 30, 'bold'), fg="#ffffff", bg="#000000")
        self.question_label.pack(pady=20)

        self.options_var = tk.IntVar()
        self.options = []
        for i, option in enumerate(question['options']):
            radio = tk.Radiobutton(self.master, text=option, variable=self.options_var, value=i + 1, font=('pixelmix', 25), fg="#33FFFF", bg="#000000")
            radio.pack(anchor='center')
            self.options.append(radio)

        self.submit_button = tk.Button(self.master, text="Submit Answer", font=("pixelmix", 30), fg="#000000", bg="#FFE732", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.timer_label = tk.Label(self.master, text=f"Time left: {self.timer} seconds", font=("pixelmix", 25), fg="#FF3232", bg="#000000")
        self.timer_label.pack(pady=10)

        self.start_timer()
     else:
        self.end_quiz()

    def check_answer(self):
        self.timer_running = False
        selected_option = self.options_var.get()
        correct_answer = self.questions[self.current_question_index]['answer']
        if selected_option == correct_answer:
            self.total_score += 1
            messagebox.showinfo("Result", "🎉 Correct! Well done! 🎉")
        else:
            correct_option_text = self.questions[self.current_question_index]['options'][correct_answer - 1]
            messagebox.showinfo("Result", f"❌ Wrong! The correct answer was: {correct_option_text} ❌")
        
        self.current_question_index += 1
        self.show_question()

    def end_quiz(self):
        self.clear_quiz_selection()
        messagebox.showinfo("Quiz Finished", f"{self.player_name}, your total score: {self.total_score}/{len(self.questions)}")
        
        self.update_leaderboard(self.player_name, self.total_score)
        
        self.display_leaderboard()
        self.clear_frame()
        self.name_label.pack()
        self.name_entry.pack(pady=5)
        self.start_button.pack(pady=20)

    def clear_quiz_selection(self):
        for widget in self.master.winfo_children():
            if widget not in [self.title_label, self.name_label, self.name_entry, self.start_button, self.bg_label]:
                widget.destroy()

    def start_timer(self):
        self.timer = 30
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running and self.timer > 0:
            self.timer_label.config(text=f"Time left: {self.timer} seconds", font=('pixelmix', 20,))
            self.timer -= 1
            self.master.after(1000, self.update_timer)
        elif self.timer_running and self.timer == 0:
            self.timer_running = False
            messagebox.showwarning("Time's Up!", "⏰ You ran out of time for this question! ⏰")
            self.current_question_index += 1
            self.show_question()

    def is_name_taken(self, name):
        return any(player['name'] == name for player in self.leaderboard)

    def update_leaderboard(self, name, score):
        self.leaderboard.append({'name': name, 'score': score})
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x['score'], reverse=True)[:5]
        self.save_leaderboard()

    def load_leaderboard(self):
        if os.path.exists("leaderboard.csv"):
            with open("leaderboard.csv", mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.leaderboard.append({'name': row['name'], 'score': int(row['score'])})

    def save_leaderboard(self):
        with open("leaderboard.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'score'])
            writer.writeheader()
            for player in self.leaderboard:
                writer.writerow(player)

    def display_leaderboard(self):
     leaderboard_str = "\n".join([f"{i+1}. {player['name']} - {player['score']} points" for i, player in enumerate(self.leaderboard)])
     self.bg_image = Image.open(r'C:\Users\Huawei Matebook\Desktop\PythonTest\3.png')
     self.bg_photo = ImageTk.PhotoImage(self.bg_image)
     self.bg_label.config(image=self.bg_photo)
     self.bg_label.image = self.bg_photo

     leaderboard_label = tk.Label(self.master, text="Leaderboard:\n\n" + leaderboard_str, font=('pixelmix', 25), fg="#ffffff", bg="#0C4C2A")
     leaderboard_label.pack(pady=20)

def main():
    
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

main()