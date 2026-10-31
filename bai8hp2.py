import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    quantity INTEGER
)
''')
conn.commit()
current_products = [] 
# Def 
def add_product():
    name = entry_name.get().strip()
    price = entry_price.get().strip()
    quantity = entry_quantity.get().strip()
    if name=="" or price=="" or quantity=="":
        messagebox.showwarning("Error", "Please fill in all fields.")
        return
    if price<0 or quantity<0:
        messagebox.showwarning("Error", "Price and quantity must be non-negative.")
        return
    cursor.execute('''INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)''',
                (name.strip(), float(price), int(quantity)))
    conn.commit()
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    messagebox.showinfo("Success", "Product added successfully.")

# Tkinter GUI
root = tk.Tk()
root.title("Product Management")
root.geometry("600x600")

title = tk.Label(
    root,
    text="PRODUCT MANAGEMENT",
    font=("Arial", 24),
    fg="blue"
)
title.pack(pady=15)

tk.Label(root, text="Name product:",font=("Arial", 14)).pack()
entry_name= tk.Entry(root, font=("Arial", 14),width=30)
entry_name.pack(pady=5)

tk.Label(root, text="Price:",font=("Arial", 14)).pack()
entry_price= tk.Entry(root, font=("Arial", 14),width=30)
entry_price.pack(pady=5)

tk.Label(root, text="Quantity:",font=("Arial", 14)).pack()
entry_quantity= tk.Entry(root, font=("Arial", 14),width=30)
entry_quantity.pack(pady=5)

button_add = tk.Button(root, text="Add Product", font=("Arial", 14), width=20,
                        command=add_product).pack(pady=5)
root.mainloop()  