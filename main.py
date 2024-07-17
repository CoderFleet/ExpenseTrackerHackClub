import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.state('zoomed')

        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 14))
        style.configure('TButton', font=('Arial', 12))

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.grid(row=0, column=0, columnspan=3, pady=20)

        self.header_label = ttk.Label(self.header_frame, text="Expense Tracker", font=("Arial", 24))
        self.header_label.pack()

        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.grid(row=1, column=0, columnspan=3, pady=10)

        self.label_amount = ttk.Label(self.input_frame, text="Amount:")
        self.label_amount.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_amount = ttk.Entry(self.input_frame)
        self.entry_amount.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_category = ttk.Label(self.input_frame, text="Category:")
        self.label_category.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_category = ttk.Entry(self.input_frame)
        self.entry_category.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_date = ttk.Label(self.input_frame, text="Date:")
        self.label_date.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_date = ttk.Entry(self.input_frame)
        self.entry_date.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.grid(row=2, column=0, columnspan=3, pady=20)

        self.button_add = ttk.Button(self.buttons_frame, text="Add Expense", command=self.add_expense)
        self.button_add.pack(side=tk.LEFT, padx=10)

        self.button_edit = ttk.Button(self.buttons_frame, text="Edit Expense", command=self.edit_expense)
        self.button_edit.pack(side=tk.LEFT, padx=10)

        self.button_delete = ttk.Button(self.buttons_frame, text="Delete Expense", command=self.delete_expense)
        self.button_delete.pack(side=tk.LEFT, padx=10)

        self.summary_frame = ttk.Frame(self.main_frame)
        self.summary_frame.grid(row=3, column=0, columnspan=3, pady=20)

        self.label_total = ttk.Label(self.summary_frame, text="Total Expenses: $0")
        self.label_total.pack()

        self.search_frame = ttk.Frame(self.main_frame)
        self.search_frame.grid(row=4, column=0, columnspan=3, pady=20)

        self.label_search = ttk.Label(self.search_frame, text="Search by Category:")
        self.label_search.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_search = ttk.Entry(self.search_frame)
        self.entry_search.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.button_search = ttk.Button(self.search_frame, text="Search", command=self.search_expenses)
        self.button_search.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)
        self.button_reset = ttk.Button(self.search_frame, text="Reset", command=self.reset_search)
        self.button_reset.grid(row=0, column=3, padx=10, pady=10, sticky=tk.W)

        self.expenses_frame = ttk.Frame(self.main_frame)
        self.expenses_frame.grid(row=5, column=0, columnspan=3, pady=20)

        self.label_expenses = ttk.Label(self.expenses_frame, text="Expenses:")
        self.label_expenses.pack()

        self.expenses_listbox = tk.Listbox(self.expenses_frame, height=20, width=80)
        self.expenses_listbox.pack()

        self.expenses = []

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Add Expense", command=self.add_expense)
        self.edit_menu.add_command(label="Edit Expense", command=self.edit_expense)
        self.edit_menu.add_command(label="Delete Expense", command=self.delete_expense)

    def add_expense(self):
        amount = self.entry_amount.get()
        category = self.entry_category.get()
        date = self.entry_date.get()

        if amount and category and date:
            expense = {"amount": amount, "category": category, "date": date}
            self.expenses.append(expense)
            self.update_expenses_display()
            self.update_total_expenses()
            self.clear_input_fields()
            messagebox.showinfo("Expense Added", f"Amount: {amount}, Category: {category}, Date: {date}")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def update_expenses_display(self):
        self.expenses_listbox.delete(0, tk.END)
        for idx, expense in enumerate(self.expenses, start=1):
            self.expenses_listbox.insert(tk.END, f"{idx}. Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

    def update_total_expenses(self):
        total = sum(float(expense['amount']) for expense in self.expenses)
        self.label_total.config(text=f"Total Expenses: ${total:.2f}")

    def clear_input_fields(self):
        self.entry_amount.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)

    def edit_expense(self):
        selected_index = self.expenses_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            selected_expense = self.expenses[idx]

            self.entry_amount.delete(0, tk.END)
            self.entry_amount.insert(0, selected_expense['amount'])

            self.entry_category.delete(0, tk.END)
            self.entry_category.insert(0, selected_expense['category'])

            self.entry_date.delete(0, tk.END)
            self.entry_date.insert(0, selected_expense['date'])

            def save_edited_expense():
                self.expenses[idx] = {
                    'amount': self.entry_amount.get(),
                    'category': self.entry_category.get(),
                    'date': self.entry_date.get()
                }
                self.update_expenses_display()
                self.update_total_expenses()
                self.clear_input_fields()
                self.button_add.config(command=self.add_expense)
                messagebox.showinfo("Expense Updated", "Expense updated successfully.")

            self.button_add.config(command=save_edited_expense)
            messagebox.showinfo("Edit Mode", "Update the fields and click 'Add Expense' to save changes.")
        else:
            messagebox.showerror("Error", "Select an expense to edit.")

    def delete_expense(self):
        selected_index = self.expenses_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            self.expenses.pop(idx)
            self.update_expenses_display()
            self.update_total_expenses()
            messagebox.showinfo("Expense Deleted", "Expense deleted successfully.")
        else:
            messagebox.showerror("Error", "Select an expense to delete.")

    def search_expenses(self):
        search_term = self.entry_search.get().lower()
        if search_term:
            filtered_expenses = [expense for expense in self.expenses if search_term in expense['category'].lower()]
            self.expenses_listbox.delete(0, tk.END)
            for idx, expense in enumerate(filtered_expenses, start=1):
                self.expenses_listbox.insert(tk.END, f"{idx}. Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")
        else:
            self.update_expenses_display()

    def reset_search(self):
        self.entry_search.delete(0, tk.END)
        self.update_expenses_display()

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
