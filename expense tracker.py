import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a database or connect to one
conn = sqlite3.connect('expenses.db')

# Create a cursor
c = conn.cursor()

# Create the expenses table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            description TEXT,
            amount REAL
            )''')

# Commit changes and close connection
conn.commit()
conn.close()

# Functions
def add_expense():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO expenses (date, description, amount) VALUES (?, ?, ?)", 
              (date_entry.get(), desc_entry.get(), amount_entry.get()))
    
    conn.commit()
    conn.close()

    # Clear the entry boxes
    date_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", "Expense Added!")
    view_expenses()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute("SELECT * FROM expenses")
    records = c.fetchall()
    
    expenses_list.delete(0, tk.END)  # Clear the listbox

    # Insert each record into the listbox with the INR symbol
    for record in records:
        expenses_list.insert(tk.END, f"{record[1]} | {record[2]} | ₹{record[3]}")
    
    conn.close()

# Set up the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create labels and entries
date_label = tk.Label(root, text="Date (DD-MM-YYYY)")
date_label.grid(row=0, column=0, padx=10, pady=10)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=10, pady=10)

desc_label = tk.Label(root, text="Description")
desc_label.grid(row=1, column=0, padx=10, pady=10)
desc_entry = tk.Entry(root)
desc_entry.grid(row=1, column=1, padx=10, pady=10)

amount_label = tk.Label(root, text="Amount (₹)")
amount_label.grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

# Add Expense Button
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Listbox to show expenses
expenses_list = tk.Listbox(root, width=50)
expenses_list.grid(row=4, column=0, columnspan=2, pady=10)

# View Expenses Button
view_button = tk.Button(root, text="View All Expenses", command=view_expenses)
view_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the application
root.mainloop()
