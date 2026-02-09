import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def organize_files(source_directory, type_mappings):
    try:
        for filename in os.listdir(source_directory):
            if os.path.isfile(os.path.join(source_directory, filename)):
                file_extension = filename.split('.')[-1].lower()

                if file_extension in type_mappings:
                    destination_directory = type_mappings[file_extension]
                else:
                    destination_directory = type_mappings['other']  # Default directory for unknown types

                create_directory_if_not_exists(destination_directory)

                shutil.move(os.path.join(source_directory, filename), os.path.join(destination_directory, filename))

        messagebox.showinfo("Success", "Files organized successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        source_directory_entry.delete(0, tk.END)
        source_directory_entry.insert(0, directory)

def start_organizing():
    source_directory = source_directory_entry.get()
    if not os.path.exists(source_directory):
        messagebox.showerror("Error", "The specified directory does not exist.")
        return

    # Dictionary mapping file types to destination directories
    type_mappings = {
        'txt': os.path.join(source_directory, 'text_files'),
        'jpg': os.path.join(source_directory, 'image_files'),
        'pdf': os.path.join(source_directory, 'pdf_files'),
        'other': os.path.join(source_directory, 'other_files')  # Default directory for unknown types
    }

    organize_files(source_directory, type_mappings)

# Create the main window
root = tk.Tk()
root.state('zoomed')
root.title("File Organizer")

# Create a frame with a light blue background
frame = tk.Frame(root, bg='lightblue')
frame.place(relwidth=1, relheight=1)

# Create and place the widgets inside the frame
tk.Label(frame, font=("Helvetica", 16), fg='black', bg='lightblue', text="Source Directory:").grid(row=0, column=0, padx=10, pady=10)

source_directory_entry = tk.Entry(frame, width=50)
source_directory_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(frame, text="Browse", font=("Helvetica", 16), fg='black', bg='lightblue', command=select_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

organize_button = tk.Button(frame, text="Organize Files", font=("Helvetica", 16), fg='black', bg='lightblue', command=start_organizing)
organize_button.grid(row=1, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()