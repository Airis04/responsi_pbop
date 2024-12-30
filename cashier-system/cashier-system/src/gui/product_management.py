from tkinter import Tk, Frame, Label, Entry, Button, Listbox, END, messagebox
from database import create_connection

class ProductManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Product Management")
        self.frame = Frame(self.master)
        self.frame.pack(pady=10)

        self.label_name = Label(self.frame, text="Product Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = Entry(self.frame)
        self.entry_name.grid(row=0, column=1)

        self.label_price = Label(self.frame, text="Product Price:")
        self.label_price.grid(row=1, column=0)
        self.entry_price = Entry(self.frame)
        self.entry_price.grid(row=1, column=1)

        self.button_add = Button(self.frame, text="Add Product", command=self.add_product)
        self.button_add.grid(row=2, column=0, columnspan=2)

        self.button_edit = Button(self.frame, text="Edit Product", command=self.edit_product)
        self.button_edit.grid(row=3, column=0, columnspan=2)

        self.button_delete = Button(self.frame, text="Delete Product", command=self.delete_product)
        self.button_delete.grid(row=4, column=0, columnspan=2)

        self.product_list = Listbox(self.frame, width=50)
        self.product_list.grid(row=5, column=0, columnspan=2)

        self.load_products()

    def load_products(self):
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, price FROM products")
            products = cursor.fetchall()
            for product in products:
                self.product_list.insert(END, f"{product[0]} - ${product[1]:.2f}")
            conn.close()

    def add_product(self):
        name = self.entry_name.get()
        price = self.entry_price.get()
        if name and price:
            conn = create_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
                conn.commit()
                conn.close()
                self.product_list.insert(END, f"{name} - ${price}")
                self.entry_name.delete(0, END)
                self.entry_price.delete(0, END)
        else:
            messagebox.showwarning("Input Error", "Please enter both name and price.")

    def edit_product(self):
        selected_product = self.product_list.curselection()
        if selected_product:
            name = self.entry_name.get()
            price = self.entry_price.get()
            if name and price:
                product_info = self.product_list.get(selected_product).split(" - ")
                old_name = product_info[0]
                conn = create_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE products SET name=%s, price=%s WHERE name=%s", (name, price, old_name))
                    conn.commit()
                    conn.close()
                    self.product_list.delete(selected_product)
                    self.product_list.insert(selected_product, f"{name} - ${price}")
                    self.entry_name.delete(0, END)
                    self.entry_price.delete(0, END)
            else:
                messagebox.showwarning("Input Error", "Please enter both name and price.")
        else:
            messagebox.showwarning("Selection Error", "Please select a product to edit.")

    def delete_product(self):
        selected_product = self.product_list.curselection()
        if selected_product:
            product_info = self.product_list.get(selected_product).split(" - ")
            name = product_info[0]
            conn = create_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM products WHERE name=%s", (name,))
                conn.commit()
                conn.close()
                self.product_list.delete(selected_product)
        else:
            messagebox.showwarning("Selection Error", "Please select a product to delete.")