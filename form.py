import tkinter as tk
from tkinter import messagebox

class RegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Registration Form")

        # Create labels and entry fields
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(master, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(master, width=30, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create register button
        self.register_button = tk.Button(master, text="Register", command=self.register_user)
        self.register_button.grid(row=3, column=1, padx=5, pady=5)

    def register_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Store the data in a database or a file (e.g., SQLite, MongoDB, etc.)
        # For this example, we'll just print the data
        print(f"Username: {username}, Email: {email}, Password: {password}")

        # Show a success message
        messagebox.showinfo("Registration", "Registration successful!")

root = tk.Tk()
my_form = RegistrationForm(root)
root.mainloop()