import sqlite3
import csv
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

conn = sqlite3.connect("delivery.db")
c = conn.cursor()

def create_tables():
    c.execute("DROP TABLE IF EXISTS Customers")
    c.execute("DROP TABLE IF EXISTS Deliveries")
    c.execute("DROP TABLE IF EXISTS Drivers")

    c.execute("""
              CREATE TABLE Customers (
                customer_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                street_address TEXT,
                suburb TEXT,
                post_code TEXT
              )
            """)
    
    c.execute("""
              CREATE TABLE Drivers (
                driver_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                street_address TEXT,
                suburb TEXT,
                post_code TEXT,
                phone_number TEXT
              )
            """)
    
    c.execute("""
              CREATE TABLE Deliveries (
                delivery_docket INTEGER PRIMARY KEY,
                collected_from TEXT,
                date_collected DATE,
                weight REAL,
                deliver_to TEXT,
                date_delivered DATE,
                customer_id INTEGER,
                driver_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
                FOREIGN KEY (driver_id) REFERENCES Drivers (driver_id)
              )
              """)
    print("Tables Created")
    conn.commit()

def import_csv_data():
    with open("customers.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            c.execute("INSERT INTO Customers (customer_id, first_name, last_name, street_address, suburb, post_code) VALUES (?, ?, ?, ?, ?, ?)", (int(row[0]), row[1], row[2], row[3], row[4], row[5]))

    with open("drivers.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            c.execute("INSERT INTO Drivers (driver_id, first_name, last_name, street_address, suburb, post_code, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6]))

    with open("deliveries.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            c.execute("INSERT INTO Deliveries (delivery_docket, collected_from, date_collected, weight, deliver_to, date_delivered, customer_id, driver_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (int(row[0]), row[1], row[2], float(row[3]), row[4], row[5], int(row[6]), int(row[7])))
    print("CSV Data Imported")
    conn.commit()

def fetch_table_data(table_name):
    c.execute(f"SELECT * FROM {table_name}")
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

    tk.Label(root, text="Welcome to the Delivery Database", font=("Arial", 18, "bold")).pack(pady=40)

    buttons = [
        ("Deliveries", "Deliveries"),
        ("Customers", "Customers"),
        ("Drivers", "Drivers"),
    ]

    for label, table in buttons:
        tk.Button(root, text=f"View {label} Table", command=lambda t=table: create_table_frame(root, t)).pack(pady=10)


create_tables()
import_csv_data()

root = tk.Tk()
root.title("Delivery Database")
root.geometry("800x600")

show_intro_screen(root)

root.mainloop()
