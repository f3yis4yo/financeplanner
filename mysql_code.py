import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Fp773kja.",
    database="bank_db"
)
cursor = mydb.cursor()

# Function to enter data into the database 
def add_customers(name, email, balance):
    sql = "INSERT INTO customers (name, email, balance) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, balance))
    mydb.commit()
    customer_id = cursor.lastrowid
    print(f"Customer added successfully! ID: {customer_id}")
    return customer_id

# Function to insert new budget into the database 
def add_budget(customer_id, category, amount, budget_date):
    sql = "INSERT INTO budget (customer_id, category, amount, budget_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (customer_id, category, amount, budget_date))
    mydb.commit()
    budget_id = cursor.lastrowid
    print(f"Budget added successfully! ID: {budget_id}")
    return budget_id

# Function to insert new expense into the database 
def add_expenses(customer_id, budget_id, category, amount, expense_date):
    sql = "INSERT INTO expenses (customer_id, budget_id, category, amount, expense_date) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (customer_id, budget_id, category, amount, expense_date))
    mydb.commit()
    print("Expense added successfully!")

# Function to insert new income into the database 
def add_income(customer_id, amount):
    sql = "INSERT INTO income (customer_id, amount) VALUES (%s, %s)"
    cursor.execute(sql, (customer_id, amount))
    mydb.commit()
    print("Income added successfully!")

# Sample data for testing (dynamic IDs to avoid hardcoding)
customer_id = add_customers("Paul", "sendpaul@sample.com", 1000.00)
budget_id = add_budget(customer_id, "Education", 200.00, "2025-03-01")
add_expenses(customer_id, budget_id, "Food", 50.00, "2025-03-02")
add_income(customer_id, 2000.00)

# Close the database connection
cursor.close()
mydb.close()
