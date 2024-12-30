from tkinter import Toplevel, Label, Entry, Button, Listbox, END, messagebox
from database import create_connection

class TransactionProcessing:
    def __init__(self, master):
        self.master = master
        self.master.title("Transaction Processing")
        
        self.product_list = Listbox(master)
        self.product_list.pack()

        self.quantity_label = Label(master, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = Entry(master)
        self.quantity_entry.pack()

        self.total_label = Label(master, text="Total Price: $0.00")
        self.total_label.pack()

        self.process_button = Button(master, text="Process Transaction", command=self.process_transaction)
        self.process_button.pack()

        self.load_products()

    def load_products(self):
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM products")
            products = cursor.fetchall()
            for product in products:
                self.product_list.insert(END, product[0])
            conn.close()

    def process_transaction(self):
        selected_product = self.product_list.get(self.product_list.curselection())
        quantity = self.quantity_entry.get()

        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Input Error", "Please enter a valid quantity.")
            return

        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT price FROM products WHERE name = %s", (selected_product,))
            price = cursor.fetchone()[0]
            total_price = price * int(quantity)

            cursor.execute("INSERT INTO transactions (product_name, quantity, total_price) VALUES (%s, %s, %s)",
                           (selected_product, quantity, total_price))
            conn.commit()
            conn.close()

            self.total_label.config(text=f"Total Price: ${total_price:.2f}")
            messagebox.showinfo("Transaction Successful", "Transaction has been processed.")
        else:
            messagebox.showerror("Database Error", "Could not connect to the database.")