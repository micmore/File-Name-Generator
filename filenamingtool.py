import tkinter as tk
from datetime import datetime

def generate_filename():
    # Retrieve current date in DD/MM/YYYY format
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    # Retrieve user input
    course_type = course_type_entry.get().strip().upper()
    course_number = course_number_entry.get().strip()
    module_chapter = module_chapter_entry.get().strip().replace(' ', '_').upper()
    assignment_name = assignment_name_entry.get().strip().replace(' ', '_').upper()
    
    # Generate the filename
    filename = f"{course_type}_{course_number}_{module_chapter}_{assignment_name}_{current_date}".replace('/', '_')
    
    # Update the filename in the text field
    filename_entry.delete(0, tk.END)  # Clear the existing content
    filename_entry.insert(0, filename)  # Insert the new filename

# Create the main window
root = tk.Tk()
root.title("File Name Generator")
root.geometry("450x450")  # Set the window size

# Create and place input fields and labels
tk.Label(root, text="Course Type (e.g., ITEC):").grid(row=0, column=0)
course_type_entry = tk.Entry(root)
course_type_entry.grid(row=0, column=1)

tk.Label(root, text="Course Number (e.g., 334):").grid(row=1, column=0)
course_number_entry = tk.Entry(root)
course_number_entry.grid(row=1, column=1)

tk.Label(root, text="Module/Chapter (e.g., Module 3):").grid(row=2, column=0)
module_chapter_entry = tk.Entry(root)
module_chapter_entry.grid(row=2, column=1)

tk.Label(root, text="Assignment Name (e.g., Data Design):").grid(row=3, column=0)
assignment_name_entry = tk.Entry(root)
assignment_name_entry.grid(row=3, column=1)

# Create and place the button
name_file_button = tk.Button(root, text="Name File", command=generate_filename)
name_file_button.grid(row=4, column=0, columnspan=2)

# Create and place the entry to display and edit the generated file name
filename_entry = tk.Entry(root)
filename_entry.grid(row=5, column=0, columnspan=2)

# Start the main loop
root.mainloop()
