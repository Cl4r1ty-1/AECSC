import sqlite3
import tkinter as tk
from tkinter import ttk

conn = sqlite3.connect("library.db")
c = conn.cursor()

def fetch_table_data(table):
    c.execute(f"SELECT * FROM {table}")
    return c.fetchall(), [description[0] for description in c.description]

def create_table_frame(root, table_name):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f'{table_name} Table', font=("Arial", 16, "bold")).pack(pady=10)

    data, columns = fetch_table_data(table_name)

    tree = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    for row in data:
        tree.insert('', tk.END, values=row)

    tree.pack(expand=True, fill='both', padx=20, pady=10)
    tk.Button(root, text='Back to Home', command=lambda: show_intro_screen(root)).pack(pady=10)

def show_intro_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Welcome to the Library Database", font=("Arial", 18, "bold")).pack(pady=40)

    buttons = [
        ("Books", "Books"),
        ("Authors", "Authors"),
        ("Genres", "Genres"),
        ("Book_Genres", "Book_Genres"),
        ("Borowers", "Borrowers")
    ]

    for label, table in buttons:
        tk.Button(root, text=f"View {table} table", width=25, command=lambda t=table: create_table_frame(root, t)).pack(pady=5)

root = tk.Tk()
root.title("Library database system")
root.geometry("800x600")

show_intro_screen(root)

root.mainloop()