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
                post_code INTEGER
              )
            """)
    
    c.execute("""
              CREATE TABLE Drivers (
                driver_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                street_address TEXT,
                suburb TEXT,
                post_code INTEGER,
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

def create_query_frame(root, query):
    for widget in root.winfo_children():
        widget.destroy()

    c.execute(query)

    data, columns = c.fetchall(), [description[0] for description in c.description]

    tree = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    for row in data:
        tree.insert('', tk.END, values=row)

    tree.pack(expand=True, fill='both', padx=20, pady=10)
    tk.Button(root, text='Back to Queries', command=lambda: query_menu(root)).pack(pady=10)


def query_1():
    c.execute("SELECT * FROM Customers WHERE Suburb LIKE 'K%'")
    return c.fetchall(), [description[0] for description in c.description]

def query_2():
    c.execute("SELECT delivery_docket, collected_from, date_collected, weight, deliver_to, date_delivered FROM Deliveries WHERE driver_id = (SELECT driver_id FROM Drivers WHERE first_name = 'Brad' AND last_name = 'Johnson')")
    return c.fetchall(), [description[0] for description in c.description]

def query_3():
    c.execute("SELECT * FROM Deliveries WHERE deliver_to = 'Subiaco' AND weight < 5")
    return c.fetchall(), [description[0] for description in c.description]

def query_4():
    c.execute("SELECT * FROM Customers WHERE post_code BETWEEN 6030 AND 6090 ORDER BY post_code DESC")
    return c.fetchall(), [description[0] for description in c.description]

def query_5():
    c.execute("")
    return c.fetchall(), [description[0] for description in c.description]

def query_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Query menu",font=("Arial", 16, "bold")).pack(pady=40)

    
    # todo: ask about inner joins, maybe do it for all deliveries (i.e include customers name and drivers name)
    queries = [
        ("List of customers' details who live in a suburb that start with a K", 
         """SELECT * FROM Customers 
            WHERE Suburb LIKE 'K%'"""),
        ("Brad Johnson's deliveries", 
         """SELECT delivery_docket, collected_from, date_collected, weight, deliver_to, date_delivered, customer_id 
            FROM Deliveries 
            WHERE driver_id = (SELECT driver_id FROM Drivers WHERE first_name = 'Brad' AND last_name = 'Johnson')"""),
        ("Deliveries under 5kg going to Subiaco", 
         """SELECT * FROM Deliveries 
            WHERE deliver_to = 'Subiaco' AND weight < 5"""),
        ("Customers in postcodes 6030-6090", 
         """SELECT * FROM Customers 
            WHERE post_code BETWEEN 6030 AND 6090 
            ORDER BY post_code DESC"""),
        ("Specific Date", 
         "query_5"), # todo
        ("Weight Range", 
         "query_6"), # todo
        ("Show heavy or light", 
         """SELECT delivery_docket, collected_from, date_collected, weight, deliver_to, date_delivered, 
            CASE 
                WHEN weight < 9 THEN 'Light' 
                WHEN weight >= 9 THEN 'Heavy' 
                ELSE 'Invalid Weight' 
            END AS weight_category 
            FROM Deliveries"""),
        ("Number of delivers and drivers", 
         """SELECT 
            (SELECT COUNT(*) FROM Deliveries) AS deliveries, 
            (SELECT COUNT(*) FROM Drivers) AS drivers"""),
        ("Average, Lowest, Highest Weight", 
         """SELECT 
            ROUND(AVG(Weight), 2) AS Average, 
            MIN(Weight) AS Lowest, 
            MAX(Weight) AS Highest 
            FROM Deliveries"""),
        ("Fees", 
         """SELECT Deliveries.delivery_docket, Deliveries.collected_from, Deliveries.date_collected, Deliveries.weight, Deliveries.deliver_to, Deliveries.date_delivered, 
            Drivers.first_name AS driver_first_name, Drivers.last_name AS driver_last_name, 
            (10+(10*weight)) AS Fee 
            FROM Deliveries 
            INNER JOIN Drivers ON Deliveries.driver_id = Drivers.driver_id"""),
        ("Mystery Package", 
         """SELECT Deliveries.delivery_docket, Deliveries.collected_from, Deliveries.date_collected, Deliveries.weight, Deliveries.deliver_to, Deliveries.date_delivered, 
            CONCAT(Customers.first_name, ' ', Customers.last_name) AS Customer
            FROM Deliveries
            INNER JOIN Customers ON Deliveries.customer_id = Customers.customer_id
            WHERE Deliveries.date_delivered > 12/01/2037 AND Deliveries.weight > 3 AND Customers.last_name LIKE 'A%'""")
    ]

    for label, query in queries:
        tk.Button(root, text=label, command=lambda q=query: create_query_frame(root, q)).pack(pady=5)

    tk.Button(root, text="Back to home", command=lambda: show_intro_screen(root)).pack(pady=10)

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

    tk.Button(root, text="Queries", command=lambda: query_menu(root)).pack(pady=10)

print("Setting up DB...")
create_tables()
import_csv_data()
print("Done")

print("Starting app...")

root = tk.Tk()
root.title("Delivery Database")
root.geometry("800x600")

show_intro_screen(root)

root.mainloop()
