from tkinter import Tk
from gui.main_window import MainWindow

def main():
    root = Tk()
    root.title("Cashier System")
    root.geometry("800x600")
    
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()