import pandas as pd
import os
from tkinter import Tk, filedialog, messagebox, Label, Button


# Initialize Tkinter
root = Tk()
root.title("Xpath finder")
root.geometry("400x300")

# Global variables
reference_file = None
process_file = None

def select_reference_file():
    """Allow user to select the reference Excel file."""
    global reference_file
    reference_file = filedialog.askopenfilename(
        title="Select the Reference Excel File",
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if reference_file:
        label_ref_file.config(text=f"Selected: {os.path.basename(reference_file)}")
        btn_next_to_process.config(state="normal")
    else:
        label_ref_file.config(text="No file selected!")

def select_process_file():
    """Allow user to select the file to process."""
    global process_file
    process_file = filedialog.askopenfilename(
        title="Select the Excel File to Process",
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if process_file:
        label_proc_file.config(text=f"Selected: {os.path.basename(process_file)}")
        btn_start_processing.config(state="normal")
    else:
        label_proc_file.config(text="No file selected!")

def start_processing():
    """Process the files and save the output."""
    global reference_file, process_file

    try:
        # Determine the output path
        output_file = os.path.join(
            os.path.dirname(process_file),
            os.path.basename(process_file).split(".")[0] + "_output.xlsx"
        )

        # Load the reference file
        reference_df = pd.read_excel(reference_file)

        # Load the file to process
        process_df = pd.read_excel(process_file)

        # Create a lookup dictionary from the reference file
        reference_lookup = dict(zip(reference_df["Donnée du modèle"], reference_df["Xpath"]))

        # Process the file
        def find_xpath(model):
            return reference_lookup.get(model, "Not Found")

        process_df["Xpath"] = process_df["Donnée du modèle"].apply(find_xpath)

        # Save the output
        process_df.to_excel(output_file, index=False)

        # Success message
        messagebox.showinfo("Success", f"Processing complete!\nOutput saved to:\n{output_file}")

    except Exception as e:
        # Error message
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI Elements
Label(root, text="Welcome to Xpath Finder!", font=("Helvetica", 14)).pack(pady=10)

# Select reference file
Label(root, text="Step 1: Select the reference Excel file:").pack(anchor="w", padx=20)
btn_ref_file = Button(root, text="Choose Reference File", command=select_reference_file)
btn_ref_file.pack(pady=5)
label_ref_file = Label(root, text="No file selected!", fg="gray")
label_ref_file.pack()

# Select process file
Label(root, text="Step 2: Select the Excel file to process:").pack(anchor="w", padx=20)
btn_next_to_process = Button(root, text="Choose Process File", command=select_process_file, state="disabled")
btn_next_to_process.pack(pady=5)
label_proc_file = Label(root, text="No file selected!", fg="gray")
label_proc_file.pack()

# Start processing
btn_start_processing = Button(root, text="Start Processing", command=start_processing, state="disabled")
btn_start_processing.pack(pady=20)

Label(root, text="© 2024 md_naciri. All rights reserved.", font=("Helvetica", 8), fg="gray").pack(side="bottom", pady=5)

# Run the GUI loop
root.mainloop()