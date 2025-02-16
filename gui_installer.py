import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

# Function to run the install/uninstall script
def run_script(option):
    try:
        result = subprocess.run(["./install_validator.sh", option], capture_output=True, text=True)

        # Display output in the text area
        output_text.insert(tk.END, result.stdout + "\n")
        output_text.yview(tk.END)  # Auto-scroll to the bottom

        if result.returncode == 0:
            messagebox.showinfo("Success", "Operation completed successfully!")
        else:
            messagebox.showerror("Error", "Something went wrong!\n" + result.stderr)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create GUI window
root = tk.Tk()
root.title("Software Installer & Validator")

# Styling
root.configure(bg="black")

# Heading
label = tk.Label(root, text="Automated Software Installer", font=("Arial", 16, "bold"), bg="black", fg="white")
label.pack(pady=10)

# Buttons
install_button = tk.Button(root, text="✅ Install Software", bg="green", fg="white", font=("Arial", 12),
                           command=lambda: run_script("1"))
install_button.pack(pady=5)

uninstall_button = tk.Button(root, text="❌ Uninstall Software", bg="red", fg="white", font=("Arial", 12),
                             command=lambda: run_script("2"))
uninstall_button.pack(pady=5)

# Text output area
output_text = scrolledtext.ScrolledText(root, width=50, height=10)
output_text.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="⬅ Exit", bg="gray", fg="white", font=("Arial", 12), command=root.quit)
exit_button.pack(pady=10)

# Run the GUI
root.mainloop()
