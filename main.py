import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        # Creating UI elements
        self.label_title = tk.Label(root, text="Expense Tracker", font=("Arial", 16))
        self.label_title.pack(pady=10)
        
        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.pack()
        self.entry_amount = tk.Entry(root)
        self.entry_amount.pack()
        
        self.label_category = tk.Label(root, text="Category:")
        self.label_category.pack()
        self.entry_category = tk.Entry(root)
        self.entry_category.pack()
        
        self.label_date = tk.Label(root, text="Date:")
        self.label_date.pack()
        self.entry_date = tk.Entry(root)
        self.entry_date.pack()
        
        self.button_add_expense = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.button_add_expense.pack(pady=10)
        
    def add_expense(self):
        amount = self.entry_amount.get()
        category = self.entry_category.get()
        date = self.entry_date.get()
        
        if amount and category and date:
            messagebox.showinfo("Expense Added", f"Amount: {amount}, Category: {category}, Date: {date}")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

# Main function to run the app
def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
