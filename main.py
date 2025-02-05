import tkinter as tk
from role_selection import open_role_selection

def main():
    global root
    root = tk.Tk()
    root.title("Tamil Nadu Welfare Connect")
    root.geometry("600x400")

    open_role_selection(root)

    root.mainloop()

if __name__ == "__main__":
    main()

