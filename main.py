import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        self.title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 16))
        self.title_label.pack(pady=10)
        
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()
        
        self.category_label = tk.Label(root, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(root)
        self.category_entry.pack()
        
        self.date_label = tk.Label(root, text="Date:")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=10)
        
        self.edit_button = tk.Button(root, text="Edit Expense", command=self.edit_expense)
        self.edit_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Expense", command=self.delete_expense)
        self.delete_button.pack()
        
        self.expenses = []
        
        self.expenses_label = tk.Label(root, text="Expenses:")
        self.expenses_label.pack()
        
        self.expenses_text = tk.Listbox(root, height=10, width=50)
        self.expenses_text.pack()
        
    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get()
        
        if amount and category and date:
            expense = {"amount": amount, "category": category, "date": date}
            self.expenses.append(expense)
            self.update_expenses_display()
            self.clear_input_fields()
            messagebox.showinfo("Expense Added", f"Amount: {amount}, Category: {category}, Date: {date}")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    
    def update_expenses_display(self):
        self.expenses_text.delete(0, tk.END)
        for idx, expense in enumerate(self.expenses, start=1):
            self.expenses_text.insert(tk.END, f"{idx}. Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")
    
    def clear_input_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
    
    def edit_expense(self):
        selected_index = self.expenses_text.curselection()
        if selected_index:
            idx = selected_index[0]
            selected_expense = self.expenses[idx]
            
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, selected_expense['amount'])
            
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, selected_expense['category'])
            
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, selected_expense['date'])
            
            def save_edited_expense():
                self.expenses[idx] = {
                    'amount': self.amount_entry.get(),
                    'category': self.category_entry.get(),
                    'date': self.date_entry.get()
                }
                self.update_expenses_display()
                self.clear_input_fields()
                self.add_button.config(command=self.add_expense)
                messagebox.showinfo("Expense Updated", "Expense updated successfully.")
            
            self.add_button.config(command=save_edited_expense)
            messagebox.showinfo("Edit Mode", "Update the fields and click 'Add Expense' to save changes.")
        else:
            messagebox.showerror("Error", "Select an expense to edit.")
    
    def delete_expense(self):
        selected_index = self.expenses_text.curselection()
        if selected_index:
            idx = selected_index[0]
            self.expenses.pop(idx)
            self.update_expenses_display()
            messagebox.showinfo("Expense Deleted", "Expense deleted successfully.")
        else:
            messagebox.showerror("Error", "Select an expense to delete.")
    
def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
