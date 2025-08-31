import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Input App")

# Function to display the typed text
def display_text():
    entered_text = text_entry.get()
    output_label.config(text=entered_text)

# Entry widget for text input
text_entry = tk.Entry(root, font=("Arial", 16), width=30)
text_entry.pack(pady=10)

# Button to trigger displaying the text
display_button = tk.Button(root, text="Display Text", command=display_text, font=("Arial", 14))
display_button.pack(pady=10)

# Label to show the output text
output_label = tk.Label(root, text="", font=("Arial", 18), fg="blue")
output_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
