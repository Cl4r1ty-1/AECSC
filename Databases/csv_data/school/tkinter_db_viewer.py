import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

conn = sqlite3.connect("school.db")
c = conn.cursor()

def show_table_data(table_name):
    try:
        # clear previous data from TreeView
        for row in tree.get_children():
            tree.delete(row)

        # fetch data
        c.execute(f"SELECT * FROM {table_name}")
        rows = c.fetchall()
        columns = [description[0] for description in c.description]

        #configure columns in Treeview
        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        #insert table rows into TreeView
        for row in rows:
            tree.insert("", tk.END, values = row)
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load table: {e}")

#create main window
root = tk.Tk()
root.title("Retail Database Viewer")

table_names = []
try:
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = [row[0] for row in c.fetchall()]
except Exception as e:
    messagebox.showerror("Error", f"Failed to fetch table names: {e}")

# create dropdown menu
selected_table = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_table, values=table_names)
dropdown.pack(pady=10)

# button to load the selected table
def load_table():
    if selected_table.get():
        show_table_data(selected_table.get())
    else:
        messagebox.showwarning("Warning", "Please select a table")

# treeview widget to display table rows
tree = ttk.Treeview(root)
tree.pack(fill=tk.BOTH, expand=True)

load_button = tk.Button(root, text="Load Table", command=load_table)
load_button.pack(pady=5)

root.mainloop()

conn.close()