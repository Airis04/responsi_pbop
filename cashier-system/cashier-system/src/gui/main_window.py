from tkinter import Tk, Frame, Button, Label, Menu
from tkinter import messagebox
from gui.product_management import ProductManagement
from gui.transaction_processing import TransactionProcessing

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Cashier System")
        self.master.geometry("800x600")

        self.create_menu()
        self.create_widgets()

        self.product_management = ProductManagement(self.master)
        self.transaction_processing = TransactionProcessing(self.master)

    def create_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        product_menu = Menu(menu)
        menu.add_cascade(label="Products", menu=product_menu)
        product_menu.add_command(label="Manage Products", command=self.open_product_management)

        transaction_menu = Menu(menu)
        menu.add_cascade(label="Transactions", menu=transaction_menu)
        transaction_menu.add_command(label="Process Transaction", command=self.open_transaction_processing)

        exit_menu = Menu(menu)
        menu.add_cascade(label="Exit", menu=exit_menu)
        exit_menu.add_command(label="Quit", command=self.master.quit)

    def create_widgets(self):
        frame = Frame(self.master)
        frame.pack(pady=20)

        label = Label(frame, text="Welcome to the Cashier System", font=("Helvetica", 16))
        label.pack()

        button_exit = Button(frame, text="Exit", command=self.master.quit)
        button_exit.pack(pady=10)

    def open_product_management(self):
        self.product_management.show()

    def open_transaction_processing(self):
        self.transaction_processing.show()

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()