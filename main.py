import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        self.label_title = tk.Label(root, text="Expense Tracker", font=("Poppins", 16))
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
        
        self.expenses = []
        
        self.label_expenses_title = tk.Label(root, text="Expenses:")
        self.label_expenses_title.pack(pady=10)
        
        self.text_expenses = tk.Text(root, height=10, width=50)
        self.text_expenses.pack()
        
    def add_expense(self):
        amount = self.entry_amount.get()
        category = self.entry_category.get()
        date = self.entry_date.get()
        
        if amount and category and date:
            expense = {"amount": amount, "category": category, "date": date}
            self.expenses.append(expense)
            self.update_expenses_display()
            self.clear_input_fields()
            messagebox.showinfo("Expense Added", f"Amount: {amount}, Category: {category}, Date: {date}")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    
    def update_expenses_display(self):
        self.text_expenses.delete(1.0, tk.END)
        for expense in self.expenses:
            self.text_expenses.insert(tk.END, f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}\n")
    
    def clear_input_fields(self):
        self.entry_amount.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
