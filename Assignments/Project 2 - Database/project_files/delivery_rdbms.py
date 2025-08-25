import sqlite3
import csv
import tkinter as tk
from tkinter import messagebox, filedialog, ttk, simpledialog
from fpdf import FPDF

conn = sqlite3.connect("delivery.db")
c = conn.cursor()

def create_tables():
    c.execute("DROP TABLE IF EXISTS Customers")
    c.execute("DROP TABLE IF EXISTS Deliveries")
    c.execute("DROP TABLE IF EXISTS Drivers")
    # to do: set NOT NULL on required values
    c.execute("""
              CREATE TABLE Customers (
                customer_id INTEGER PRIMARY KEY NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT,
                street_address TEXT NOT NULL,
                suburb TEXT NOT NULL,
                post_code INTEGER NOT NULL
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

    if query == 'query_5':
        try:
            specific_date = simpledialog.askstring("Specific Date", "Enter date (DD/MM/YYYY): ", initialvalue="01/01/2000")
            # todo: input handling
            c.execute("""
                    SELECT Deliveries.delivery_docket, Deliveries.collected_from, Deliveries.date_collected, Deliveries.weight, Deliveries.deliver_to, Deliveries.date_delivered,
                    CONCAT(Drivers.first_name, ' ', Drivers.last_name) AS driver,
                    CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer
                    FROM Deliveries
                    INNER JOIN Drivers ON Deliveries.driver_id = Drivers.driver_id
                    INNER JOIN Customers ON Deliveries.customer_id = Customers.customer_id
                    WHERE Deliveries.date_delivered = ?
                    """, (specific_date,))
        except Exception as e:
            messagebox.showerror("Invalid input", "Please enter a valid date in the correct format")
    elif query == 'query_6':
        low_weight = simpledialog.askfloat("Low Weight", "Enter the minimum weight: ")
        high_weight = simpledialog.askfloat("High Weight", "Enter the maximum weight: ")
        c.execute("""
                 SELECT Deliveries.weight, Drivers.* FROM Deliveries 
                 INNER JOIN Drivers ON Deliveries.driver_id = Drivers.driver_id 
                 WHERE Deliveries.weight BETWEEN ? AND ?
                 """, (low_weight, high_weight))
    else:
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


def query_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Query menu",font=("Arial", 16, "bold")).pack(pady=40)

    queries = [
        ("List of customers' details who live in a suburb that start with a K", 
         """SELECT * FROM Customers 
            WHERE Suburb LIKE 'K%'"""),
        ("Brad Johnson's deliveries", 
         """SELECT delivery_docket, collected_from, date_collected, weight, deliver_to, date_delivered 
            FROM Deliveries 
            WHERE driver_id = (SELECT driver_id FROM Drivers WHERE first_name = 'Brad' AND last_name = 'Johnson')"""),
        ("Deliveries under 5kg going to Subiaco", 
         """SELECT Deliveries.delivery_docket, Deliveries.collected_from, Deliveries.date_collected, Deliveries.weight, Deliveries.date_delivered,
            CONCAT(Drivers.first_name, ' ', Drivers.last_name) AS driver
            FROM Deliveries
            INNER JOIN Drivers ON Deliveries.driver_id = Drivers.driver_id
            WHERE Deliveries.deliver_to = 'Subiaco' AND Deliveries.weight < 5"""),
        ("Customers in postcodes 6030-6090", 
         """SELECT * FROM Customers 
            WHERE post_code BETWEEN 6030 AND 6090 
            ORDER BY post_code DESC"""),
        ("Delivery Details from a Specific Date", 
         "query_5"),
        ("Driver Details based on a range of package weights", 
         "query_6"),
        ("Show heavy or light", 
         """SELECT delivery_docket, collected_from, date_collected, weight, deliver_to, date_delivered, 
            CASE 
                WHEN weight < 9 THEN 'Light' 
                WHEN weight >= 9 THEN 'Heavy' 
                ELSE 'Invalid Weight' 
            END AS weight_category 
            FROM Deliveries"""),
        ("Number of deliveries and drivers", 
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
         """SELECT Deliveries.delivery_docket, Deliveries.collected_from, Deliveries.date_collected, Deliveries.weight, (10+(10*weight)) AS Fee, Deliveries.deliver_to, Deliveries.date_delivered, 
            CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer,
            CONCAT(Drivers.first_name, ' ', Drivers.last_name) AS driver
            FROM Deliveries 
            INNER JOIN Drivers ON Deliveries.driver_id = Drivers.driver_id
            INNER JOIN Customers ON Deliveries.customer_id = Customers.customer_id"""),
        ("Mystery Package", 
         """SELECT Deliveries.delivery_docket, Deliveries.collected_from, Deliveries.date_collected, Deliveries.weight, Deliveries.deliver_to, Deliveries.date_delivered, 
            CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer
            FROM Deliveries
            INNER JOIN Customers ON Deliveries.customer_id = Customers.customer_id
            WHERE Deliveries.date_delivered > 12/01/2037 AND Deliveries.weight > 3 AND Customers.last_name LIKE 'A%'""")
    ]

    for label, query in queries:
        tk.Button(root, text=label, command=lambda q=query: create_query_frame(root, q)).pack(pady=5)

    tk.Button(root, text="Back to home", command=lambda: show_intro_screen(root)).pack(pady=10)

def export_to_pdf(label, qurey):
    c.execute(qurey)

    headers = [desc[0] for desc in c.description]
    data = c.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Delivery Report", ln=True, align="C")
    pdf.cell(0, 10, label, ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    col_width = pdf.w / (len(headers) + 1) 
    row_height = 10

    for header in headers:
        pdf.cell(col_width, row_height, header, border=1, align="C")
    pdf.ln(row_height)

    pdf.set_font("Arial", "", 11)
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height, str(item), border=1, align="C")
        pdf.ln(row_height)

    pdf.output('test.pdf', "F")

def export_to_csv(query):
    c.execute(query)
    results = c.fetchall()

    if not results:
        messagebox.showerror("No results", "No data to export")
        return
    
    filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not filepath:
        messagebox.showerror("No folder chosen", "Please select a valid filepath")
        return
    
    try:
        with open(filepath, 'w+', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([desc[0] for desc in c.description])
            writer.writerows(results)
        messagebox.showinfo("Success", f"Report exported to {filepath}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_report_frame(root, label, query):
    for widget in root.winfo_children():
        widget.destroy()

    c.execute(query)
    
    data, columns = c.fetchall(), [desc[0] for desc in c.description]

    tree = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    for row in data:
        tree.insert('', tk.END, values=row)

    tree.pack(expand=True, fill='both', padx=20, pady=10)
    tk.Button(root, text="Export to CSV", command=lambda q=query: export_to_csv(q)).pack(pady=10)
    tk.Button(root, text="Export to PDF", command=lambda l=label, q=query: export_to_pdf(l, q)).pack(pady=10)
    tk.Button(root, text='Back to Home', command=lambda: show_intro_screen(root)).pack(pady=10)

def report_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    queries = [
        ("Deliveries from Belmont over 3.5kg",
         """
         SELECT Deliveries.delivery_docket AS "Delivery Docket", Deliveries.collected_from AS "Suburb Collected From", Deliveries.date_collected AS "Date Collected by Courier", Deliveries.weight AS "Weight of Package (KG)", Deliveries.deliver_to AS "Suburb Delivered To", Deliveries.date_delivered AS "Date Delivered",
         CONCAT(Drivers.first_name, ' ', Drivers.last_name) AS Driver,
         CONCAT(Customers.first_name, ' ', Customers.last_name) AS Customer
         FROM Deliveries
         INNER JOIN Drivers ON Deliveries.driver_id = Drivers.driver_id
         INNER JOIN Customers ON Deliveries.customer_id = Customers.customer_id
         WHERE Deliveries.collected_from = 'Belmont' AND Deliveries.weight > 3.5"""),
         ("Driver details that have picked up packages from 10/01/37 to 12/01/37",
          """
          SELECT Deliveries.date_collected AS "Date Collected", 
          Drivers.first_name AS "First Name", Drivers.last_name AS "Last Name", Drivers.street_address AS "Street Address", Drivers.Suburb AS "Suburb", Drivers.post_code AS "Post Code", Drivers.phone_number AS "Phone Number"
          FROM Deliveries
          INNER JOIN Drivers ON Deliveries.driver_id = Drivers.driver_id
          WHERE Deliveries.date_collected BETWEEN '10/01/2037' AND '12/01/2037'""")
    ]
    tk.Label(root, text="Report Menu", font=("Arial", 16, "bold")).pack(pady=10)

    for label, qurey in queries:
        tk.Button(root, text=label, command=lambda q=qurey, l=label: create_report_frame(root, l, q)).pack(pady=10)

    tk.Button(root, text="Back to Home", command=lambda: show_intro_screen(root)).pack(pady=10, padx=10)
    

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
    tk.Button(root, text="Reports", command=lambda: report_menu(root)).pack(pady=10)

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
conn.close()
print("DB Connection Closed")