import csv
import sqlite3

conn = sqlite3.connect('retail.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Products')
c.execute('DROP TABLE IF EXISTS Sales')

c.execute("""
          CREATE TABLE Products (
              ProductID INTEGER PRIMARY KEY,
              ProductName TEXT,
              Price REAL
          )
          """
          )


c.execute("""
          CREATE TABLE Sales (
              SaleID INTEGER PRIMARY KEY,
              ProductID INTEGER,
              Quantity INTEGER,
              SaleDate TEXT,
              FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
          )
          """
          )

# Load Products data from CSV
with open('products.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        c.execute('INSERT INTO Products (ProductID, ProductName, Price) VALUES (?, ?, ?)', row)

# Load Sales data from CSV
with open('sales.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        c.execute('INSERT INTO Sales (SaleID, ProductID, Quantity, SaleDate) VALUES (?, ?, ?, ?)', row)

# Commit changes
conn.commit()

print("Database created and data loaded successfully.")

# SQL Queries
print("1. Select all products")
c.execute('SELECT * FROM Products')
for row in c.fetchall():
    print(row)

#insert query
new_product_name = 'Shoes'
new_price = 50
c.execute(f"INSERT INTO Products (ProductName, Price) VALUES ('{new_product_name}', {new_price})")
conn.commit()
print(f"Inserted new product: '{new_product_name}' with price {new_price}")

#delete query
sale_id_to_delete = 3
c.execute(f"DELETE FROM Sales WHERE SaleID = {sale_id_to_delete}")
conn.commit()
print(f"Deleted sale with SaleID: {sale_id_to_delete}")

#update query
new_price_for_jeans = 45
c.execute(f"UPDATE Products SET Price = {new_price_for_jeans} WHERE ProductName = 'Jeans'")
conn.commit()
print("Updated price for 'Jeans' to", new_price_for_jeans)

#order by
print("\n ORDER BY price descending")
c.execute('SELECT * FROM Products ORDER BY Price DESC')
for row in c.fetchall():
    print(row)

#inner join
print("\n INNER JOIN - Sales with Product Names")
join_query = """
        SELECT Sales.SaleID, Products.ProductName, Sales.Quantity, Sales.SaleDate
        FROM Sales
        INNER JOIN Products ON Sales.ProductID = Products.ProductID
"""
c.execute(join_query)
join_results = c.fetchall()
for row in join_results:
    print(row)


# Aggregate functions
#count the number of products
print("\n COUNT total products")
c.execute('SELECT COUNT(*) FROM Products')
print(c.fetchone())

output_file = 'sales_with_product_details.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    #write header
    writer.writerow(['SaleID', 'ProductName', 'Quantity', 'SaleDate'])
    #write rows
    writer.writerows(join_results)

print("Your CSV file has been created.")
conn.close()
print("Database connection closed")