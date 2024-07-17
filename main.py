import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.attributes('-fullscreen', True)  # Full-screen mode

        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 14))
        style.configure('TButton', font=('Arial', 12))

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.title_label = ttk.Label(self.main_frame, text="Expense Tracker", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.amount_label = ttk.Label(self.main_frame, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.category_label = ttk.Label(self.main_frame, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.category_entry = ttk.Entry(self.main_frame)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.date_label = ttk.Label(self.main_frame, text="Date:")
        self.date_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        self.date_entry = ttk.Entry(self.main_frame)
        self.date_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Buttons
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        self.add_button = ttk.Button(self.button_frame, text="Add Expense", command=self.add_expense)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.edit_button = ttk.Button(self.button_frame, text="Edit Expense", command=self.edit_expense)
        self.edit_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Expense", command=self.delete_expense)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.expenses_label = ttk.Label(self.main_frame, text="Expenses:")
        self.expenses_label.grid(row=5, column=0, columnspan=3, pady=20)

        self.expenses_text = tk.Listbox(self.main_frame, height=20, width=80)
        self.expenses_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        self.expenses = []

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
