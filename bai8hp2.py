import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database
conn = sqlite3.connect('shop1.db')
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
# Def 
def display_products():
    listbox.delete(0, tk.END)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for p in products:
        p_id = p[0]
        p_name = p[1]
        p_price = p[2]
        p_quantity = p[3]

        text = f"ID: {p_id} | Name: {p_name} | Price: {p_price} | Quantity: {p_quantity}"
        listbox.insert(tk.END, text)

def add_product():
    name = entry_name.get().strip()
    price = float(entry_price.get())
    quantity = int(entry_quantity.get())
    if name=="" or price=="" or quantity=="":
        messagebox.showwarning("Error", "Please fill in all fields.")
        return
    if price<=0 or quantity<=0:
        messagebox.showwarning("Error", "Price and quantity must be positive.")
        return
    cursor.execute('''INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)''',
                (name.strip(), float(price), int(quantity)))
    conn.commit()
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    display_products()
    messagebox.showinfo("Success", "Product added successfully.")

def delete_product():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Please select a product to delete.")
        return
    index = selected[0]
    product_text = listbox.get(index)
    product_id = int(product_text.split('|')[0].split(':')[1].strip())
    cursor.execute('DELETE FROM products WHERE id=?', (product_id,))
    conn.commit()
    display_products()
    messagebox.showinfo("Success", "Product deleted successfully.")
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

listbox = tk.Listbox(root, font=("Arial", 14), width=50, height=5)
listbox.pack(pady=10)

button_delete1 = tk.Button(root, text="Delete Product", font=("Arial", 14),
                            width=20, command=delete_product).pack(pady=5)

display_products()

root.mainloop()  