import tkinter as tk
from tkinter import messagebox

# store answers
user_answers = {}

# Question 1
def question_one():
    def submit_q1():
        user_answers['Q1'] = entry.get()
        window.destroy()
        question_two()

    window = tk.Tk()
    window.title("Question 1")
    window.geometry("500x200")

    tk.Label(window, text="1. What does SQL stand for?", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(window, width=40)
    entry.pack(pady=5)

    tk.Button(window, text="Next", command=submit_q1, bg='blue', fg='white').pack(pady=10)
    window.mainloop()

# Question 2
def question_two():
    def submit_q2():
        user_answers["Q2"] = mcq_var.get()
        window.destroy()
        show_summary()

    window = tk.Tk()
    window.title("Question 2")
    window.geometry("500x250")

    tk.Label(window, text="2. Which SQL command is used to remove a table?", font=("Arial", 12)).pack(pady=10)

    mcq_var = tk.StringVar()
    mcq_var.set(None)

    options = {
        ("INSERT", "INSERT"),
        ("DELETE", "DELETE"),
        ("DROP", "DROP"),
        ("UPDATE", "UPDATE")
    }

    for text, value in options:
        tk.Radiobutton(window, text=text, variable=mcq_var, value=value).pack(anchor='w')

    tk.Button(window, text="Submit", command=submit_q2, bg='green', fg='white').pack(pady=10)
    window.mainloop()

# final summary
def show_summary():
    summary = "\n".join([f"{q}: {ans}" for q, ans in user_answers.items()])
    messagebox.showinfo("Quiz completed", "\n\nYour answers:\n" + summary)

# start quiz
question_one()