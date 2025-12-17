import sqlite3

# Connect to database
conn = sqlite3.connect("phone_company.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model TEXT,
    price REAL,
    quantity INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_number TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone_id INTEGER,
    customer_id INTEGER,
    sale_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS service_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_name TEXT,
    price REAL,
    duration TEXT
)
""")

# Function to get all phone company information
def get_all_information():
    print("\n--- Phones Inventory ---")
    for row in cursor.execute("SELECT * FROM phones"):
        print(row)

    print("\n--- Customers ---")
    for row in cursor.execute("SELECT * FROM customers"):
        print(row)

    print("\n--- Sales ---")
    for row in cursor.execute("SELECT * FROM sales"):
        print(row)

    print("\n--- Service Plans ---")
    for row in cursor.execute("SELECT * FROM service_plans"):
        print(row)

# Run function
get_all_information()

# Close database
conn.close()
