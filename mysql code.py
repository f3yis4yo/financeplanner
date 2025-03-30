import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Fp773kja.",
    database="finance_db"
)
cursor =mydb.cursor()

#Function to enter data into the database 
def add_customer(name, email, balance):
    sql ="INSERT INTO customers(name, email, balance) Values(%s, %s, %s)"
    cursor.execute(sql, (name, email, balance))
    conn.commit()
    print("Customer added successfully!")
    
#Function to insert new transaction/budget into the database 
def add_budget(customer_id, category, amount, budget_date):
    sql ="INSERT INTO budget(customer_id, category, amount, budget_date) Values(%s, %s, %s, %s)"
    cursor.execute(sql, (customer_id, category, amount, budget_date))
    conn.commit()
    print("Budget added successfully!")
    
#Function to insert new expense into the database 
def add_expense(customer_id, budget_id, category, amount, expense_date):
    sql ="INSERT INTO budget(customer_id, category, amount, budget_date) Values(%s, %s, %s, %s, %s)"
    cursor.execute(sql, (customer_id, budget_id, category, amount, expense_date))
    conn.commit()
    print("Expense added successfully!")
    
#Function to insert new income into the database 
def add_income(customer_id, amount, income_date):
    sql ="INSERT INTO budget(customer_id, category, amount, budget_date) Values(%s, %s, %s)"
    cursor.execute(sql, (customer_id, amount, income_date))
    conn.commit()
    print("Income added successfully!")

