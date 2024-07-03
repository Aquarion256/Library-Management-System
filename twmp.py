import tkinter as tk
from tkinter import messagebox
import sqlite3

class MemberWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Member Window")
        self.root.geometry("400x300")
        # Label and Entry for book search
        self.label_search = tk.Label(root, text="Search Book:")
        self.label_search.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_search = tk.Entry(root)
        self.entry_search.grid(row=0, column=1, padx=10, pady=5)
        
        # Search button
        self.button_search = tk.Button(root, text="Search", command=self.search_book)
        self.button_search.grid(row=0, column=2, padx=10, pady=5)
        
    def search_book(self):
        book_title = self.entry_search.get()
        # Connect to database
        conn = sqlite3.connect('LMS.db')
        c = conn.cursor()
        # Search for the book in Books table
        c.execute("SELECT * FROM Books WHERE book_title=?", (book_title,))
        book = c.fetchone()
        # Close database connection
        conn.close()
        if book:
            if book[3] == 'a':
                messagebox.showinfo("Book Status", "The book is available.")
            elif book[3] == 'i':
                messagebox.showinfo("Book Status", "The book is issued.")
        else:
            messagebox.showerror("Error", "Book not found.")

class EmployeeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Window")
        self.root.geometry("400x300")
        
        # Add, Remove, Update buttons
        self.button_add_book = tk.Button(root, text="Add Book", command=self.add_book)
        self.button_add_book.grid(row=0, column=0, padx=10, pady=5)
        
        self.button_remove_book = tk.Button(root, text="Remove Book", command=self.remove_book)
        self.button_remove_book.grid(row=0, column=1, padx=10, pady=5)
        
        self.button_update_book = tk.Button(root, text="Update Book", command=self.update_book)
        self.button_update_book.grid(row=0, column=2, padx=10, pady=5)
        
    def add_book(self):
        messagebox.showinfo("Info", "Add Book functionality")
        
    def remove_book(self):
        messagebox.showinfo("Info", "Remove Book functionality")
        
    def update_book(self):
        messagebox.showinfo("Info", "Update Book functionality")

class AdminWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Window")
        self.root.geometry("400x300")
        # Manage Employees and Members buttons
        self.button_manage_employees = tk.Button(root, text="Manage Employees", command=self.manage_employees)
        self.button_manage_employees.grid(row=0, column=0, padx=10, pady=5)
        
        self.button_manage_members = tk.Button(root, text="Manage Members", command=self.manage_members)
        self.button_manage_members.grid(row=0, column=1, padx=10, pady=5)
        
    def manage_employees(self):
        # Open Employee management window
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Manage Employees")
        employee_window.geometry("400x300")  # Set window size
        
        # Label and Entry for employee details
        self.label_emp_id = tk.Label(employee_window, text="Employee ID:")
        self.label_emp_id.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_emp_id = tk.Entry(employee_window)
        self.entry_emp_id.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_emp_name = tk.Label(employee_window, text="Employee Name:")
        self.label_emp_name.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_emp_name = tk.Entry(employee_window)
        self.entry_emp_name.grid(row=1, column=1, padx=10, pady=5)
        
        self.label_emp_designation = tk.Label(employee_window, text="Designation:")
        self.label_emp_designation.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_emp_designation = tk.Entry(employee_window)
        self.entry_emp_designation.grid(row=2, column=1, padx=10, pady=5)
        
        # Add, Remove, Update buttons
        self.button_add_employee = tk.Button(employee_window, text="Add Employee", command=self.add_employee)
        self.button_add_employee.grid(row=3, column=0, padx=10, pady=5)
        
        self.button_remove_employee = tk.Button(employee_window, text="Remove Employee", command=self.remove_employee)
        self.button_remove_employee.grid(row=3, column=1, padx=10, pady=5)
        
        self.button_update_employee = tk.Button(employee_window, text="Update Employee", command=self.update_employee)
        self.button_update_employee.grid(row=3, column=2, padx=10, pady=5)
        
    def manage_members(self):
        # Open Member management window
        member_window = tk.Toplevel(self.root)
        member_window.title("Manage Members")
        member_window.geometry("400x300")  # Set window size
        
        # Label and Entry for member details
        self.label_mem_id = tk.Label(member_window, text="Member ID:")
        self.label_mem_id.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_mem_id = tk.Entry(member_window)
        self.entry_mem_id.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_mem_name = tk.Label(member_window, text="Member Name:")
        self.label_mem_name.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_mem_name = tk.Entry(member_window)
        self.entry_mem_name.grid(row=1, column=1, padx=10, pady=5)
        
        self.label_mem_address = tk.Label(member_window, text="Member Address:")
        self.label_mem_address.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_mem_address = tk.Entry(member_window)
        self.entry_mem_address.grid(row=2, column=1, padx=10, pady=5)
        
        # Add, Remove, Update buttons
        self.button_add_member = tk.Button(member_window, text="Add Member", command=self.add_member)
        self.button_add_member.grid(row=3, column=0, padx=10, pady=5)
        
        self.button_remove_member = tk.Button(member_window, text="Remove Member", command=self.remove_member)
        self.button_remove_member.grid(row=3, column=1, padx=10, pady=5)
        
        self.button_update_member = tk.Button(member_window, text="Update Member", command=self.update_member)
        self.button_update_member.grid(row=3, column=2, padx=10, pady=5)
        
    def add_employee(self):
        # Get employee details from entry fields
        emp_id = self.entry_emp_id.get()
        emp_name = self.entry_emp_name.get()
        emp_designation = self.entry_emp_designation.get()
        
        # Connect to database
        conn = sqlite3.connect('LMS.db')
        c = conn.cursor()
        
        # Insert new employee record into Employee table
        c.execute("INSERT INTO Employee (emp_id, emp_name, designation) VALUES (?, ?, ?)", (emp_id, emp_name, emp_designation))
        
        # Commit changes and close database connection
        conn.commit()
        conn.close()
        
        # Show success message
        messagebox.showinfo("Success", "Employee added successfully.")
        
        # Clear entry fields
        self.entry_emp_id.delete(0, tk.END)
        self.entry_emp_name.delete(0, tk.END)
        self.entry_emp_designation.delete(0, tk.END)
        
    def remove_employee(self):
        messagebox.showinfo("Info", "Remove Employee functionality")
        
    def update_employee(self):
        messagebox.showinfo("Info", "Update Employee functionality")
        
    def add_member(self):
        messagebox.showinfo("Info", "Add Member functionality")
        
    def remove_member(self):
        messagebox.showinfo("Info", "Remove Member functionality")
        
    def update_member(self):
        messagebox.showinfo("Info", "Update Member functionality")

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System - Login")
        self.root.geometry("400x300")
        # Label and Entry for username
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)
        
        # Label and Entry for password
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)
        
        # Radio buttons for selecting login role
        self.login_role = tk.StringVar()
        self.admin_radio = tk.Radiobutton(root, text="Admin", variable=self.login_role, value="admin")
        self.admin_radio.grid(row=2, column=0, padx=10, pady=5)
        self.employee_radio = tk.Radiobutton(root, text="Employee", variable=self.login_role, value="employee")
        self.employee_radio.grid(row=2, column=1, padx=10, pady=5)
        self.member_radio = tk.Radiobutton(root, text="Member", variable=self.login_role, value="member")
        self.member_radio.grid(row=2, column=2, padx=10, pady=5)
        
        # Login button
        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=tk.NSEW)
        
    def login(self):
        # Get username, password, and selected login role
        username = self.entry_username.get()
        password = self.entry_password.get()
        role = self.login_role.get()
        
        # Connect to database
        conn = sqlite3.connect('LMS.db')
        c = conn.cursor()
        
        # Check login credentials based on selected role
        if role == "admin":
            c.execute("SELECT * FROM Admin WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            if user:
                # Close database connection
                conn.close()
                # Open Admin window
                self.root.destroy()
                admin_window = tk.Tk()
                admin_app = AdminWindow(admin_window)
                admin_window.mainloop()
                return
        elif role == "employee":
            c.execute("SELECT * FROM Employee WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            if user:
                # Close database connection
                conn.close()
                # Open Employee window
                self.root.destroy()
                employee_window = tk.Tk()
                employee_app = EmployeeWindow(employee_window)
                employee_window.mainloop()
                return
        elif role == "member":
            c.execute("SELECT * FROM Member WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            if user:
                # Close database connection
                conn.close()
                # Open Member window
                self.root.destroy()
                member_window = tk.Tk()
                member_app = MemberWindow(member_window)
                member_window.mainloop()
                return
        else:
            messagebox.showerror("Error", "Please select a login role")
            return
        
        # Close database connection
        conn.close()
        # Show error message if login fails
        messagebox.showerror("Error", "Invalid username or password")


# Function to create the database and tables
def create_database():
    # Connect to or create the database
    conn = sqlite3.connect('LMS.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS Library (
                    lib_id INTEGER PRIMARY KEY,
                    lib_name TEXT,
                    lib_address TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Admin (
                    admin_id INTEGER PRIMARY KEY,
                    admin_role TEXT,
                    admin_name TEXT,
                    username TEXT,
                    password TEXT,
                    lib_id INTEGER,
                    FOREIGN KEY (lib_id) REFERENCES Library(lib_id) ON DELETE CASCADE
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Employee (
                    emp_id INTEGER PRIMARY KEY,
                    emp_name TEXT,
                    designation TEXT,
                    username TEXT,
                    password TEXT,
                    lib_id INTEGER,
                    FOREIGN KEY (lib_id) REFERENCES Library(lib_id) ON DELETE CASCADE
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Member (
                    mem_id INTEGER PRIMARY KEY,
                    mem_name TEXT,
                    mem_address TEXT,
                    username TEXT,
                    password TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Books (
                    book_id INTEGER PRIMARY KEY,
                    book_title TEXT,
                    book_price REAL,
                    book_status TEXT,
                    aut_id INTEGER,
                    pub_id INTEGER,
                    lib_id INTEGER,
                    FOREIGN KEY (aut_id) REFERENCES Author(aut_id) ON DELETE CASCADE,
                    FOREIGN KEY (pub_id) REFERENCES Publisher(pub_id) ON DELETE CASCADE,
                    FOREIGN KEY (lib_id) REFERENCES Library(lib_id) ON DELETE CASCADE
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Author (
                    aut_id INTEGER PRIMARY KEY,
                    aut_name TEXT,
                    aut_subject TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Publisher (
                    pub_id INTEGER PRIMARY KEY,
                    pub_name TEXT,
                    pub_country TEXT
                )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the function to create the database and tables
create_database()


root = tk.Tk()
app = LoginApp(root)
root.mainloop()